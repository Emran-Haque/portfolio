# Profile Image

## Setup Instructions

The portfolio is configured to display a profile image at `static/images/profile.jpg`. 

### What You Need to Do:

1. **Prepare Your Image:**
   - Use the profile photo you provided (the one shown earlier with the winter jacket)
   - **Remove the background** - Use tools like:
     - [remove.bg](https://www.remove.bg) - Free online tool
     - Photoshop, GIMP, Figma, or similar software
   - **Crop to half-body** - Show from shoulders up to knees (side view, left-facing)
   - **Export as JPG** - File should be approximately 400x500px or larger

2. **Place the Image:**
   - Save the processed image as `profile.jpg` in this directory (`static/images/`)
   - The templates will automatically use it at `{% static 'images/profile.jpg' %}`

3. **CSS Styling (Already Applied):**
   The image is automatically styled in the hero section with:
   - Professional rounded corners (`rounded-xl`)
   - Subtle gradient background (blur effect)
   - Responsive sizing (hidden on mobile, visible on desktop)
   - Proper cropping using CSS `object-fit: cover` and `object-position: top center`

## Image Display Locations

- **Home Page:** Hero section (right side, desktop only)
- **About Page:** Profile card (sticky sidebar)

## Technical Notes

The image styling uses modern CSS:
```css
.hero-photo {
    rounded-xl /* 12px border radius */
    object-fit: cover
    object-position: top center
}
```

No external image manipulation tools are needed—once you place the image here, it will be properly styled by the CSS.

## Preview

The image will appear in a beautiful frame with a gradient shadow effect on all pages that reference it.
