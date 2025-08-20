#!/bin/bash

echo "🚀 Quarterly Earnings Presentation Deployment Guide"
echo "=================================================="
echo ""

echo "📋 Prerequisites:"
echo "1. GitHub account"
echo "2. Git configured with your credentials"
echo ""

echo "🔧 Deployment Steps:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Repository name: quarterly-earnings-presentation"
echo "   - Make it public (required for free GitHub Pages)"
echo "   - Don't initialize with README (we already have one)"
echo ""

echo "2. Connect your local repository to GitHub:"
echo "   git remote add origin https://github.com/[YOUR_USERNAME]/quarterly-earnings-presentation.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""

echo "3. Enable GitHub Pages:"
echo "   - Go to your repository on GitHub"
echo "   - Click Settings tab"
echo "   - Scroll to Pages section"
echo "   - Source: Deploy from a branch"
echo "   - Branch: main"
echo "   - Folder: / (root)"
echo "   - Click Save"
echo ""

echo "4. Your presentation will be available at:"
echo "   https://[YOUR_USERNAME].github.io/quarterly-earnings-presentation/"
echo ""

echo "⏰ Note: GitHub Pages can take 5-10 minutes to deploy initially"
echo ""

echo "🔄 To refresh cached content, add version parameters:"
echo "   ?v=1, ?v=2, etc. to the URL"
echo ""

echo "📧 Contact: 23f2005402@ds.study.iitm.ac.in"
echo ""

read -p "Press Enter to continue..."
