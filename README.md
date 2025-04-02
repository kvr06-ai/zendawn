# ZenDawn - Mindful Travel Experiences

A modern, responsive travel blog sharing authentic travel experiences with a focus on cultural connections, mindful exploration, and language learning across the globe, starting with India.

## Live Site

Visit [ZenDawn.me](https://zendawn.me) to explore the blog.

## Features

- Modern, clean design with beautiful imagery
- Fully responsive layout for all devices
- SEO-optimized content structure with proper metadata
- Region-based navigation for global destinations (currently focusing on India)
- Rich storytelling with personal experiences and practical information
- Interactive elements like comment sections for community engagement
- Optimized images for faster loading without sacrificing quality
- Newsletter integration for building an audience

## Current Content

### Destinations
- **India**
  - Bhimbetka Rock Shelters (Madhya Pradesh) - Comprehensive guide with history, visitor information, and personal experiences
  - More destinations coming soon (Hampi, Varanasi, Sikkim, etc.)

### Planned Content
- Additional Indian destinations
- Expansion to Southeast Asia (Thailand, Vietnam, Cambodia)
- Japan travel guides
- Travel style guides (solo travel, cultural immersion, language learning trips)
- Practical tips for mindful travelers

## Technical Features

- HTML5 and CSS3 with modern design patterns
- Vanilla JavaScript for interactive elements
- Optimized image pipeline that reduces file sizes by 90%+
- LocalStorage for comment persistence
- Responsive design breakpoints for mobile, tablet, and desktop
- Newsletter integration with Mailchimp

## Getting Started

### Prerequisites

- Node.js (v14.0.0 or higher)
- npm (v6.0.0 or higher)

### Installation

1. Clone the repository
2. Navigate to the project directory:
   ```
   cd website-travel
   ```
3. Install dependencies:
   ```
   npm install
   ```

### Running Locally

Start the development server:
```
npm run dev
```

The site will be served at `http://localhost:8080` and will automatically reload when you make changes to the source files.

### Optimizing Images

The repository includes an image optimization script that significantly reduces image file sizes:

```
python scripts/optimize_images.py
```

This will automatically convert PNG files to optimized JPGs and place them in the appropriate optimized-images directory.

## Project Structure

```
website-travel/
├── src/                # Source files
│   ├── css/            # CSS styles
│   ├── js/             # JavaScript files
│   ├── destinations-india/ # India destination guides
│   │   ├── bhimbhetka/ # Bhimbetka Rock Shelters guide
│   │   └── ...         # Other destination guides
│   ├── optimized-images/ # Compressed image assets 
│   ├── travel-styles/  # Different ways to experience travel
│   ├── about/          # About the author and the blog
│   ├── policies/       # Privacy policy and terms
│   └── index.html      # Main HTML file
├── scripts/            # Utility scripts
│   └── optimize_images.py # Image optimization utility
├── package.json        # Project dependencies and scripts
└── README.md           # Project documentation
```

## Deployment

This project is configured for deployment with GitHub and Netlify.

### Deployment Steps

1. Push code to your GitHub repository:
   ```
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

2. Sign in to [Netlify](https://app.netlify.com/) with your GitHub account
3. Connect your repository and configure build settings:
   - Publish directory: `src`

## Future Development

- Backend integration for comment system (replacing localStorage)
- Search functionality across all content
- Interactive maps for destination discovery
- Related articles recommendations
- Dark mode support
- Accessibility improvements
- Performance optimizations
- Translation support for multiple languages

## Contributing

This is a personal project, but suggestions and feedback are welcome through the comment system on the blog or by opening issues in the GitHub repository.

## License

© 2025 ZenDawn. All rights reserved. The content and design of this website are protected by copyright law. 