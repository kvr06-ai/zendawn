# ZenDawn - Mindful Travel in India

A modern, responsive travel blog focused on mindful travel experiences across India.

## Features

- Modern, clean design
- Fully responsive layout
- SEO-optimized content structure
- Region-based navigation for Indian destinations
- Categories for different travel styles
- Practical travel tips section
- Personal travel stories

## Getting Started

### Prerequisites

- Node.js (v12.0.0 or higher)
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
npm start
```

The site will be served at `http://localhost:8080` and will automatically reload when you make changes to the source files.

## Project Structure

```
website-travel/
├── src/                # Source files
│   ├── css/            # CSS styles
│   ├── js/             # JavaScript files
│   ├── images/         # Image assets
│   ├── destinations-india/ # India destination guides
│   ├── travel-styles/  # Different ways to experience India
│   ├── practical-tips/ # Travel tips and advice
│   ├── mindful-travel/ # Mindful travel philosophy
│   ├── stories/        # Personal travel narratives
│   └── index.html      # Main HTML file
├── package.json        # Project dependencies and scripts
└── README.md           # Project documentation
```

## Deployment

This project is configured for easy deployment with Netlify and GitHub.

### Deployment Steps

1. Push this code to your GitHub repository:
   ```
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

2. Sign in to [Netlify](https://app.netlify.com/) with your GitHub account
3. Click "New site from Git" and select your GitHub repository
4. In the deploy settings:
   - Build command: Leave empty (as configured in netlify.toml)
   - Publish directory: `src`
   - Click "Deploy site"

5. Configure your custom domain:
   - Go to "Domain settings" for your new site
   - Click "Add custom domain"
   - Enter: `zendawn.me`
   - Follow the prompts to verify ownership

## Customization

- **Colors**: Edit the CSS variables in `src/css/styles.css` to change the color scheme
- **Content**: Update the HTML in `src/index.html` and other files to change text content and layout
- **Images**: Replace placeholder images in the `src/images` directory with your own travel photos

## SEO Optimization

The blog has been set up with SEO best practices in mind:
- Semantic HTML structure
- Meta description
- Mobile-friendly design
- Fast loading times

See `seo_guidelines.md` for detailed SEO strategies to implement. 