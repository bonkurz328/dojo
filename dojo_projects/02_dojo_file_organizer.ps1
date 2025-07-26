function Organize-Downloads {
    $downloadsPath = "$UserProfile\<DownloadsFolder>"  # e.g.: "Downloads"
    $logFile = "$downloadsPath\OrganizerLog_$(Get-Date -Format 'yyyyMMdd').txt"

    $folders = @{
        "Images"    = @("*.jpg", "*.jpeg", "*.png", "*.gif", "*.webp")
        "Documents" = @("*.pdf", "*.docx", "*.xlsx", "*.pptx", "*.txt", "*.md")
        "Archives"  = @("*.zip", "*.rar", "*.7z", "*.tar.gz")
        "Music"     = @("*.mp3", "*.wav", "*.flac")
        "Videos"    = @("*.mp4", "*.mov", "*.avi")
        "Scripts"   = @("*.ps1", "*.sh", "*.py", "*.go", "*.js")
    }

    # Create folders if they don't exist 
    foreach ($folder in $folders.Keys) {
        $fullPath = Join-Path -Path $downloadsPath -ChildPath $folder
        if (!(Test-Path -Path $fullPath)) {
            New-Item -Path $fullPath -ItemType Directory | Out-Null
        }
    }

    # Move files to their respective folders 
    foreach ($folder in $folders.Keys) {
        $extensions = $folders[$folder]
        foreach ($ext in $extensions) {
            Get-ChildItem -Path $downloadsPath -Filter $ext -File | ForEach-Object {
                try {
                    Move-Item -Path $_.FullName -Destination "$downloadsPath\$folder" -ErrorAction Stop
                    "$(Get-Date) - Moved $($_.Name) to $folder" | Out-File $logFile -Append
                } catch {
                    Write-Warning "Failed to move $($_.Name): $_"
                }
            }
        }
    }

    Write-Host "Downloads folder organized! 📂 Log: $logFile" -ForegroundColor Green
}
