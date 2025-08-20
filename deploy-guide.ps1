# Quarterly Earnings Presentation Deployment Guide
# PowerShell Script for Windows

Write-Host "🚀 Quarterly Earnings Presentation Deployment Guide" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "📋 Prerequisites:" -ForegroundColor Yellow
Write-Host "1. GitHub account"
Write-Host "2. Git configured with your credentials"
Write-Host ""

Write-Host "🔧 Deployment Steps:" -ForegroundColor Green
Write-Host ""

Write-Host "1. Create a new repository on GitHub:" -ForegroundColor White
Write-Host "   - Go to https://github.com/new"
Write-Host "   - Repository name: quarterly-earnings-presentation"
Write-Host "   - Make it public (required for free GitHub Pages)"
Write-Host "   - Don't initialize with README (we already have one)"
Write-Host ""

Write-Host "2. Connect your local repository to GitHub:" -ForegroundColor White
Write-Host "   Execute these commands in this directory:" -ForegroundColor Gray
Write-Host "   git remote add origin https://github.com/[YOUR_USERNAME]/quarterly-earnings-presentation.git" -ForegroundColor Magenta
Write-Host "   git branch -M main" -ForegroundColor Magenta
Write-Host "   git push -u origin main" -ForegroundColor Magenta
Write-Host ""

Write-Host "3. Enable GitHub Pages:" -ForegroundColor White
Write-Host "   - Go to your repository on GitHub"
Write-Host "   - Click Settings tab"
Write-Host "   - Scroll to Pages section"
Write-Host "   - Source: Deploy from a branch"
Write-Host "   - Branch: main"
Write-Host "   - Folder: / (root)"
Write-Host "   - Click Save"
Write-Host ""

Write-Host "4. Your presentation will be available at:" -ForegroundColor White
Write-Host "   https://[YOUR_USERNAME].github.io/quarterly-earnings-presentation/" -ForegroundColor Green
Write-Host ""

Write-Host "⏰ Note: GitHub Pages can take 5-10 minutes to deploy initially" -ForegroundColor Yellow
Write-Host ""

Write-Host "🔄 To refresh cached content, add version parameters:" -ForegroundColor Cyan
Write-Host "   ?v=1, ?v=2, etc. to the URL"
Write-Host ""

Write-Host "📧 Contact: 23f2005402@ds.study.iitm.ac.in" -ForegroundColor Blue
Write-Host ""

# Open the presentation locally
Write-Host "🌐 Opening local preview..." -ForegroundColor Green
Start-Process "index.html"

Read-Host "Press Enter to continue"
