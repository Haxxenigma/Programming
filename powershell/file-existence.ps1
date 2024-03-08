$exists = Test-Path -Path 'C:\file.txt'

if ($exists) {
    Remove-Item -Path 'C:\file.txt' -Force
    Write-Host 'File deleted'
} else {
    New-Item -ItemType 'file' -Path 'C:\file.txt'
    Write-Host 'File created'
}