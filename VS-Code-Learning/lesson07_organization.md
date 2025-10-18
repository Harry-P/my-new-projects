# Lesson 7: Organizing Like a Pro 📁

**Time:** 25-30 minutes | **Difficulty:** Easy ⭐⭐

---

## 🎯 What You'll Learn Today

By the end of this lesson, you'll know how to:
- ✅ Create organized project folder structures
- ✅ Manage multiple files and pages
- ✅ Link pages together
- ✅ Use professional file organization
- ✅ Build a complete multi-page website

---

## 📂 Why Organization Matters

Imagine your school locker:

```
MESSY LOCKER:                  ORGANIZED LOCKER:
┌─────────────┐               ┌─────────────┐
│ 📚📝🎮📖💾 │               │  📚 Books    │
│ 🎒📱📓🖊️📄 │      VS       │  📝 Papers   │
│ 🗒️💿📕✏️📋 │               │  🎮 Fun      │
│ Everything  │               │  ✏️ Supplies │
│ mixed up!   │               │  Everything  │
│             │               │  has a place!│
└─────────────┘               └─────────────┘
   Can't find                    Easy to find
    anything!                     everything!
```

**Same with code projects!** Organization = Success 🎯

---

## 🏗️ Professional Project Structure

Here's how real developers organize projects:

```
my-website/
├── index.html          ← Home page (always index.html!)
├── about.html          ← About page
├── contact.html        ← Contact page
│
├── css/                ← All CSS files here
│   ├── style.css
│   └── themes.css
│
├── js/                 ← All JavaScript files here
│   ├── main.js
│   └── animations.js
│
├── images/             ← All images here
│   ├── logo.png
│   ├── photo1.jpg
│   └── background.jpg
│
└── README.md           ← Project description
```

---

## 🎮 Activity 1: Create Your Project Structure

Let's build a proper project!

### Step 1: Create the Main Folder

```
IN VS CODE:
1. File → Open Folder
2. Choose or create: "my-first-website"
3. Click "Select Folder"
```

### Step 2: Create Subfolders

```
Right-click in Explorer → New Folder

Create these folders:
📁 css
📁 js  
📁 images
```

### Step 3: Create Your Files

```
Right-click in Explorer → New File

In root folder:
📄 index.html
📄 about.html
📄 contact.html

In css folder:
📄 style.css

In js folder:
📄 main.js
```

### Your Structure Should Look Like:

```
MY-FIRST-WEBSITE/
├── 📁 css/
│   └── 📄 style.css
├── 📁 js/
│   └── 📄 main.js
├── 📁 images/
├── 📄 index.html
├── 📄 about.html
└── 📄 contact.html
```

---

## 🔗 Linking Files Together

### Linking HTML Pages:

```html
<!-- In index.html -->
<nav>
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="contact.html">Contact</a>
</nav>
```

### Linking CSS Files:

```html
<!-- In your HTML <head> section -->
<link rel="stylesheet" href="css/style.css">
                              ↑
                        folder/filename
```

### Linking JavaScript Files:

```html
<!-- Before closing </body> tag -->
<script src="js/main.js"></script>
                ↑
          folder/filename
```

---

## 🌐 Activity 2: Build a Multi-Page Website

Let's create a complete website!

### index.html (Home Page):

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Awesome Website</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Navigation - Same on all pages! -->
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
    </nav>
    
    <!-- Main Content -->
    <header>
        <h1>Welcome to My Website! 🌟</h1>
        <p>This is my first multi-page website!</p>
    </header>
    
    <main>
        <section>
            <h2>What You'll Find Here</h2>
            <ul>
                <li>Information about me</li>
                <li>My projects and interests</li>
                <li>Ways to contact me</li>
            </ul>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 My Website. Made with ❤️</p>
    </footer>
    
    <script src="js/main.js"></script>
</body>
</html>
```

### about.html:

```html
<!DOCTYPE html>
<html>
<head>
    <title>About Me - My Website</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
    </nav>
    
    <header>
        <h1>About Me</h1>
    </header>
    
    <main>
        <section>
            <h2>Hi, I'm [Your Name]!</h2>
            <p>I'm a 9th grader learning web development.</p>
            
            <h3>My Skills</h3>
            <ul>
                <li>HTML</li>
                <li>CSS</li>
                <li>JavaScript</li>
            </ul>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 My Website</p>
    </footer>
    
    <script src="js/main.js"></script>
</body>
</html>
```

### contact.html:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact - My Website</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
    </nav>
    
    <header>
        <h1>Get in Touch</h1>
    </header>
    
    <main>
        <section>
            <h2>Contact Information</h2>
            <p>Feel free to reach out!</p>
            
            <form>
                <label>Name:</label><br>
                <input type="text" placeholder="Your name"><br><br>
                
                <label>Email:</label><br>
                <input type="email" placeholder="your@email.com"><br><br>
                
                <label>Message:</label><br>
                <textarea rows="5" placeholder="Your message"></textarea><br><br>
                
                <button type="button" onclick="submitForm()">Send Message</button>
            </form>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2025 My Website</p>
    </footer>
    
    <script src="js/main.js"></script>
</body>
</html>
```

### css/style.css:

```css
/* Universal Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Navigation */
nav {
    background-color: #2c3e50;
    padding: 15px;
    text-align: center;
}

nav a {
    color: white;
    text-decoration: none;
    padding: 10px 20px;
    margin: 0 5px;
    border-radius: 5px;
    transition: background-color 0.3s;
}

nav a:hover {
    background-color: #34495e;
}

/* Header */
header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
    padding: 60px 20px;
}

header h1 {
    font-size: 48px;
    margin-bottom: 10px;
}

/* Main Content */
main {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
}

section {
    background-color: white;
    padding: 30px;
    margin-bottom: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h2 {
    color: #2c3e50;
    margin-bottom: 15px;
}

/* Lists */
ul {
    padding-left: 20px;
}

li {
    margin: 10px 0;
}

/* Forms */
input, textarea {
    width: 100%;
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
}

button {
    background-color: #3498db;
    color: white;
    padding: 12px 30px;
    border: none;
    border-radius: 5px;
    font-size: 18px;
    cursor: pointer;
}

button:hover {
    background-color: #2980b9;
}

/* Footer */
footer {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 50px;
}
```

### js/main.js:

```javascript
// Function for contact form
function submitForm() {
    alert("Thanks for your message! (This is just a demo)");
}

// Add active class to current page link
document.addEventListener('DOMContentLoaded', function() {
    const currentPage = window.location.pathname.split('/').pop();
    const links = document.querySelectorAll('nav a');
    
    links.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.style.backgroundColor = '#34495e';
        }
    });
});

console.log("Website loaded successfully! 🚀");
```

---

## 📝 File Naming Best Practices

### Good Names ✅

```
index.html              ← Homepage
about.html              ← About page
style.css               ← Main styles
main.js                 ← Main JavaScript
header-image.jpg        ← Descriptive
```

### Bad Names ❌

```
page1.html              ← Not descriptive
My File.html            ← Has space!
STYLES.CSS              ← All caps hard to read
asdf.js                 ← Meaningless
image (1).jpg           ← Has space and ()
```

### Rules:
- Use lowercase
- Use hyphens (-) or underscores (_) instead of spaces
- Be descriptive
- Use proper extensions (.html, .css, .js)

---

## 🗺️ Understanding File Paths

```
ABSOLUTE PATH (full address):
C:/Users/You/Documents/my-website/css/style.css

RELATIVE PATH (from current file):
css/style.css           ← Go into css folder
../index.html           ← Go up one folder
images/logo.png         ← Go into images folder
```

### Visual Guide:

```
Current file: index.html

To link style.css:
index.html → css/ → style.css
Write: css/style.css

Current file: css/style.css  

To link back to index.html:
css/style.css → ../ → index.html
Write: ../index.html
```

---

## 🎯 Lesson Summary

### What We Learned:

```
✅ How to create organized folder structures
✅ Separating HTML, CSS, and JS files
✅ Linking files together properly
✅ Building multi-page websites
✅ File naming best practices
✅ Understanding file paths
```

---

## 🏆 Challenge Complete!

You're ready for Lesson 8 if you can:

- [ ] Create a proper folder structure
- [ ] Link HTML, CSS, and JS files
- [ ] Build a multi-page website
- [ ] Navigate between pages
- [ ] Use relative file paths correctly

---

## 📚 Homework

### Task 1: Expand Your Website
```
Add these new pages:
- [ ] projects.html (show your projects)
- [ ] hobbies.html (your hobbies)
- [ ] gallery.html (collection of items)
Update navigation on ALL pages!
```

### Task 2: Organization Challenge
```
Create a complete website about:
- Your favorite hobby
- Include: home, about, gallery, contact
- Use proper folder structure
- Style consistently across all pages
```

---

## 🚀 What's Next?

In **[Lesson 8: Cool Shortcuts](lesson08_shortcuts.md)**, you'll learn keyboard shortcuts to code faster!

---

**Ready to speed up your coding? Let's go to [Lesson 8!](lesson08_shortcuts.md)**
