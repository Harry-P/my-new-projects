# 📁 Lesson 7: Project Organization Practice

## 🎯 Build a Multi-Page Website Structure!

Create a complete project with proper organization.

---

## ✅ Project Setup: Personal Website

**YOUR TASK:** Create this exact folder structure

```
my-personal-website/
├── index.html
├── about.html
├── projects.html
├── contact.html
├── css/
│   ├── style.css
│   └── animations.css
├── js/
│   ├── main.js
│   └── theme.js
├── images/
│   └── (your images here)
└── README.md
```

---

## 📋 Step-by-Step Instructions

### STEP 1: Create Main Folder

1. File → Open Folder
2. Create new folder: **"my-personal-website"**
3. Open it in VS Code

**Completed?** ☐ Yes

---

### STEP 2: Create Subfold

ers

Create these folders inside your project:

1. Right-click in Explorer → New Folder
2. Create: **css**
3. Create: **js**
4. Create: **images**

**All folders created?** ☐ Yes

---

### STEP 3: Create HTML Files

Create these files in the ROOT (main folder):

1. **index.html** - Your home page
2. **about.html** - About you
3. **projects.html** - Your projects
4. **contact.html** - Contact information

**All HTML files created?** ☐ Yes

---

### STEP 4: Create CSS Files

Create these inside the **css** folder:

1. **style.css** - Main styles
2. **animations.css** - Animation effects

**CSS files in correct folder?** ☐ Yes

---

### STEP 5: Create JavaScript Files

Create these inside the **js** folder:

1. **main.js** - Main JavaScript
2. **theme.js** - Theme switcher code

**JS files in correct folder?** ☐ Yes

---

### STEP 6: Create README

Create **README.md** in the root folder with this content:

```markdown
# My Personal Website

A website built while learning VS Code!

## Structure

- index.html - Home page
- about.html - About me
- projects.html - My projects
- contact.html - Contact form

## Technologies

- HTML
- CSS
- JavaScript

## Date Created

October 18, 2025
```

**README created?** ☐ Yes

---

## ✅ Exercise 2: Linking Files Together

**YOUR TASK:** Add navigation to link pages

### In index.html, add:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Website - Home</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="projects.html">Projects</a>
        <a href="contact.html">Contact</a>
    </nav>
    
    <h1>Welcome to My Website!</h1>
    
    <script src="js/main.js"></script>
</body>
</html>
```

### In css/style.css, add:

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
}

nav {
    background-color: #333;
    padding: 10px;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
}
```

### In js/main.js, add:

```javascript
console.log("Website loaded successfully!");

// Welcome message
alert("Welcome to my website!");
```

**All files linked correctly?** ☐ Yes

**Test:** Open index.html in browser - does CSS work? ☐ Yes ☐ No

---

## ✅ Exercise 3: Create a Blog Structure

**YOUR TASK:** Add a blog section

Create this structure inside your project:

```
blog/
├── index.html (blog home)
├── post1.html
├── post2.html
└── post3.html
```

**Blog folder created?** ☐ Yes

---

## ✅ Exercise 4: Organization Checklist

Check your project organization:

**File Organization:**
- [ ] All HTML files in root folder
- [ ] All CSS files in css folder
- [ ] All JS files in js folder
- [ ] Images in images folder
- [ ] README in root

**Naming Conventions:**
- [ ] All lowercase file names
- [ ] No spaces in file names
- [ ] Consistent naming style

**File Linking:**
- [ ] CSS linked correctly
- [ ] JS linked correctly
- [ ] Navigation works

---

## ✅ Exercise 5: Multi-Project Organization

**YOUR TASK:** Create a projects folder structure

Go back to your main VS Code folder and create:

```
VS-Code-Projects/
├── Project1-Website/
│   ├── index.html
│   ├── css/
│   └── js/
├── Project2-Calculator/
│   ├── calculator.html
│   ├── css/
│   └── js/
└── Project3-Game/
    ├── game.html
    ├── css/
    └── js/
```

**All project folders created?** ☐ Yes

---

## ✅ Exercise 6: Practice Opening Projects

**YOUR TASK:** Learn to switch between projects

1. File → Open Folder
2. Open Project1-Website
3. Work on it
4. File → Open Folder
5. Open Project2-Calculator

**Can you switch projects easily?** ☐ Yes

---

## ✅ Exercise 7: Create a Practice Template

**YOUR TASK:** Make a reusable template

Create a folder called **"project-template"** with:

```
project-template/
├── index.html (basic HTML structure)
├── css/
│   └── style.css (basic styles)
├── js/
│   └── main.js (starter code)
├── images/
└── README.md (template text)
```

Now you can COPY this template for new projects!

**Template created?** ☐ Yes

---

## 📊 Organization Assessment

**Count your files:**

Total HTML files: _______
Total CSS files: _______
Total JS files: _______
Total projects: _______

**Organization Score:**
- All files in correct folders: +5 points
- Good naming conventions: +5 points
- Working links: +5 points
- README files: +5 points

**My score:** _______ / 20

---

## 🎉 Lesson 7 Complete!

You've learned:
- ✅ How to organize project folders
- ✅ Where to put different file types
- ✅ How to link files together
- ✅ How to manage multiple projects
- ✅ Professional folder structures

**Next Step:** Lesson 8 - Master Keyboard Shortcuts!
