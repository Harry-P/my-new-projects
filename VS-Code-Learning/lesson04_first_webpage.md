# Lesson 4: Your First Webpage 🌐

**Time:** 30-35 minutes | **Difficulty:** Medium ⭐⭐⭐

---

## 🎯 What You'll Learn Today

By the end of this lesson, you'll know how to:
- ✅ Understand what HTML is (it's easier than you think!)
- ✅ Create your very first webpage
- ✅ Use basic HTML tags to structure content
- ✅ View your webpage in a real web browser
- ✅ Build a page about yourself

---

## 🌐 What is a Webpage?

Every website you visit (YouTube, Google, Instagram) is made of webpages. And guess what? **You can make them too!**

### How Webpages Work:

```
YOU TYPE CODE          BROWSER READS IT        YOU SEE A WEBPAGE
    (HTML)          →    (Like Chrome)      →    (Pretty website!)

┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ <h1>Hello</h1>│  →  │   Browser    │  →  │              │
│              │      │   Magic! ✨  │      │    Hello     │
│              │      │              │      │   (BIG TEXT) │
└──────────────┘      └──────────────┘      └──────────────┘
```

---

## 📝 What is HTML?

**HTML** stands for **HyperText Markup Language**

Don't worry about the fancy name! Think of HTML as:
- **Instructions** for how to build a webpage
- **Building blocks** like LEGO pieces
- **Labels** that tell the browser what everything is

### HTML Uses "Tags" - Like Labels:

```
Regular Text:  Hello, my name is Alex

HTML Version:  <p>Hello, my name is Alex</p>
               ↑                          ↑
            Opening tag              Closing tag

The <p> tag means "this is a paragraph"
```

---

## 🏗️ Understanding HTML Tags

Tags are like containers. They wrap around your content:

```
ANATOMY OF AN HTML TAG:

<tagname>Your content goes here</tagname>
   ↑            ↑                   ↑
Opening      Content            Closing
  tag                             tag


EXAMPLE TAGS:

<h1>Big Heading</h1>           ← Makes BIG text
<p>A paragraph</p>             ← Makes a paragraph
<strong>Bold text</strong>     ← Makes text bold
<em>Italic text</em>           ← Makes text italic
```

---

## 🎮 Activity 1: Create Your First HTML File

Let's make a real webpage!

### Step 1: Create a New File

```
IN VS CODE:
1. Click File → New File (or Ctrl + N)
2. Save it immediately! (Ctrl + S)
3. Name it: my_first_page.html
   (Notice the .html extension!)
4. VS Code will recognize it's a webpage! 🌐
```

### Step 2: Write the Basic HTML Structure

Every webpage needs this skeleton. Copy this into your file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Webpage</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my very first webpage!</p>
</body>
</html>
```

### Understanding the Structure:

```
┌─────────────────────────────────────────┐
│ <!DOCTYPE html>                         │ ← Tells browser: "This is HTML5"
├─────────────────────────────────────────┤
│ <html>                                  │ ← Everything goes inside
│   ┌─────────────────────────────────┐   │
│   │ <head>                          │   │ ← Information ABOUT the page
│   │   <title>Page Title</title>     │   │   (Not shown on page)
│   │ </head>                         │   │
│   └─────────────────────────────────┘   │
│   ┌─────────────────────────────────┐   │
│   │ <body>                          │   │ ← What SHOWS on the page
│   │   <h1>Heading</h1>              │   │
│   │   <p>Paragraph</p>              │   │
│   │ </body>                         │   │
│   └─────────────────────────────────┘   │
│ </html>                                 │
└─────────────────────────────────────────┘
```

---

## 🌟 Activity 2: View Your Webpage!

Now let's see your creation in a browser!

### Method 1: Right-Click and Open

```
IN VS CODE:
1. Right-click on "my_first_page.html" 
   in the file explorer (left side)
2. Select "Reveal in File Explorer"
3. Double-click the file
4. It opens in your default browser!
5. 🎉 YOU MADE A WEBPAGE!
```

### Method 2: Use Live Server (Recommended!)

```
INSTALL LIVE SERVER EXTENSION:
┌─────────────────────────────────────┐
│ 1. Click Extensions (📦) or Ctrl+Shift+X │
│ 2. Search "Live Server"             │
│ 3. Click "Install"                  │
│ 4. Right-click your HTML file       │
│ 5. Select "Open with Live Server"   │
│ 6. Auto-refreshes when you save! ✨ │
└─────────────────────────────────────┘
```

---

## 📚 Common HTML Tags Reference

Here are the building blocks you'll use most:

### Headings (6 Sizes):

```html
<h1>Biggest Heading</h1>     ← Like a chapter title
<h2>Second Biggest</h2>      ← Like a section
<h3>Third Biggest</h3>       ← Like a sub-section
<h4>Fourth</h4>
<h5>Fifth</h5>
<h6>Smallest Heading</h6>

WHAT THEY LOOK LIKE:
━━━━━━━━━━━━━━━━━━━━━━━━━
 H1: HUGE TEXT
━━━━━━━━━━━━━━━━━━━━━━━━━
 H2: Big Text
━━━━━━━━━━━━━━━━━━━━━━━━━
 H3: Medium Text
 H4: Regular Size
 H5: Small
 H6: Tiny
```

### Text Formatting:

```html
<p>This is a paragraph.</p>
<strong>This is bold text</strong>
<em>This is italic text</em>
<br>                              ← Line break (no closing tag!)
<hr>                              ← Horizontal line (no closing tag!)

EXAMPLE:
<p>I <strong>really</strong> love coding!</p>
→ Shows: I really love coding!
           ↑↑↑↑↑↑
           (bold)
```

### Lists:

```html
UNORDERED LIST (bullets):
<ul>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>

SHOWS AS:
• First item
• Second item  
• Third item

ORDERED LIST (numbers):
<ol>
    <li>First item</li>
    <li>Second item</li>
</ol>

SHOWS AS:
1. First item
2. Second item
```

### Links and Images:

```html
LINK (goes to another page):
<a href="https://www.google.com">Click here to go to Google</a>
      ↑                           ↑
    Where to go              What user sees

IMAGE:
<img src="photo.jpg" alt="Description of image">
     ↑               ↑
  Image file     Text if image doesn't load
```

---

## 🎨 Activity 3: Build Your "About Me" Page

Now let's create something personal! 

### Your Mission:

Create a webpage about yourself with:
- ✅ Your name as the main heading
- ✅ A paragraph about yourself
- ✅ Your favorite things in a list
- ✅ At least one link
- ✅ Some bold or italic text

### Template to Get Started:

```html
<!DOCTYPE html>
<html>
<head>
    <title>About Me - [Your Name]</title>
</head>
<body>
    <h1>[Your Name]</h1>
    
    <h2>About Me</h2>
    <p>
        Hi! I'm [your name] and I'm learning to code! 
        I'm in 9th grade and I love [your interests].
    </p>
    
    <h2>My Favorite Things</h2>
    <ul>
        <li>[Favorite food]</li>
        <li>[Favorite movie]</li>
        <li>[Favorite hobby]</li>
    </ul>
    
    <h2>What I'm Learning</h2>
    <p>
        Right now I'm learning <strong>HTML</strong> and 
        <strong>VS Code</strong>. It's pretty cool!
    </p>
    
    <h2>My Goals</h2>
    <ol>
        <li>Learn to make websites</li>
        <li>Create my own projects</li>
        <li>Share them with friends</li>
    </ol>
    
    <hr>
    <p>
        <em>Thanks for visiting my page!</em>
    </p>
</body>
</html>
```

**Save this as:** `about_me.html`

---

## 🔍 How HTML Tags Work Together

Think of HTML tags like Russian nesting dolls:

```
BIG DOLL (html)
├─ MEDIUM DOLL (body)
│  ├─ SMALL DOLL (h1)
│  ├─ SMALL DOLL (p)
│  └─ SMALL DOLL (ul)
│     ├─ TINY DOLL (li)
│     ├─ TINY DOLL (li)
│     └─ TINY DOLL (li)

IN CODE:
<html>
  <body>
    <h1>Title</h1>
    <p>Text</p>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </body>
</html>
```

**Golden Rule:** Always close tags in the opposite order you opened them!

---

## 💡 Pro Tips: Writing HTML

### Tip 1: Indentation Makes It Readable

```
BAD (Hard to read):
<html><head><title>Page</title></head><body><h1>Hi</h1></body></html>

GOOD (Easy to read):
<html>
  <head>
    <title>Page</title>
  </head>
  <body>
    <h1>Hi</h1>
  </body>
</html>
```

**VS Code helps you!** Press `Shift + Alt + F` to auto-format your code!

### Tip 2: Use Comments

```html
<!-- This is a comment. Browsers ignore it. -->
<!-- Use comments to explain your code! -->

<h1>My Page</h1>  <!-- Main heading -->
<p>Some text</p>  <!-- Description paragraph -->
```

### Tip 3: Emmet Shortcuts (Super Fast!)

In VS Code, type this and press `Tab`:

```
Type: html:5
Press: Tab
→ Creates entire HTML structure automatically! 🚀

Type: ul>li*3
Press: Tab
→ Creates list with 3 items instantly!
```

---

## 🧠 Understanding Check!

**Question 1:** What does HTML stand for?
- A) How To Make Links
- B) HyperText Markup Language ✅
- C) Home Tool Markup Language
- D) Happy Text Making Language

**Question 2:** Which tag makes the BIGGEST heading?
- A) `<h6>`
- B) `<h3>`
- C) `<h1>` ✅
- D) `<big>`

**Question 3:** What's the correct way to write a paragraph?
- A) `<paragraph>Text</paragraph>`
- B) `<p>Text</p>` ✅
- C) `[p]Text[/p]`
- D) `{p}Text{/p}`

**Question 4:** Which tag creates a bullet list?
- A) `<ol>`
- B) `<ul>` ✅
- C) `<list>`
- D) `<bullets>`

*(Answers: B, C, B, B)*

---

## 🎯 Lesson Summary

### What We Learned:

```
✅ HTML is the language of webpages
✅ Tags are like containers with opening and closing parts
✅ Every webpage has <html>, <head>, and <body>
✅ Headings go from <h1> (biggest) to <h6> (smallest)
✅ Lists can be ordered (<ol>) or unordered (<ul>)
✅ We can view HTML files in any web browser
✅ VS Code has shortcuts to help us write HTML faster
```

---

## 🏆 Challenge Complete!

You're ready for Lesson 5 if you can:

- [ ] Create a new HTML file
- [ ] Write the basic HTML structure from memory
- [ ] Use at least 5 different HTML tags
- [ ] View your webpage in a browser
- [ ] Create an "About Me" page with lists and links
- [ ] Explain what `<h1>`, `<p>`, and `<ul>` do

---

## 📚 Homework: Expand Your Page!

### Task 1: Add More Content 📝
Add these to your "About Me" page:
```html
- [ ] A "My Schedule" section with your classes
- [ ] A "Favorite Websites" section with links
- [ ] A "Future Goals" section with ordered list
- [ ] At least 3 headings
- [ ] At least 5 paragraphs
```

### Task 2: Create New Pages 🌐
Make these additional pages:
```
1. my_hobbies.html - Write about your hobbies
2. favorite_books.html - List your favorite books/movies
3. my_skills.html - Skills you have or want to learn
```

### Task 3: Experiment! 🧪
Try these challenges:
```
- [ ] Nest a list inside another list
- [ ] Use all 6 heading sizes on one page
- [ ] Create a page with at least 3 external links
- [ ] Make some text bold AND italic at the same time
```

**Hint for bold + italic:**
```html
<strong><em>This text is both!</em></strong>
```

---

## 🎨 HTML Tag Cheat Sheet

Keep this handy while coding:

| Tag | Purpose | Example |
|-----|---------|---------|
| `<h1>` to `<h6>` | Headings | `<h1>Main Title</h1>` |
| `<p>` | Paragraph | `<p>Some text</p>` |
| `<strong>` | Bold text | `<strong>Important!</strong>` |
| `<em>` | Italic text | `<em>Emphasis</em>` |
| `<ul>` | Bullet list | `<ul><li>Item</li></ul>` |
| `<ol>` | Numbered list | `<ol><li>First</li></ol>` |
| `<li>` | List item | `<li>List item</li>` |
| `<a>` | Link | `<a href="url">Link</a>` |
| `<img>` | Image | `<img src="pic.jpg">` |
| `<br>` | Line break | `Line 1<br>Line 2` |
| `<hr>` | Horizontal line | `<hr>` |

---

## 🚀 What's Next?

In **[Lesson 5: Making It Pretty](lesson05_styling.md)**, you'll:
- Learn CSS (makes webpages colorful!)
- Add colors, fonts, and styles
- Make your webpage look professional
- Create beautiful designs

**Get excited - this is where it gets really fun!** 🎨

---

## 💭 Reflection

Before moving on, think about:
1. What was the coolest thing you created today?
2. Which HTML tag is your favorite so far?
3. What would you like to add to your webpage?

---

## 🎁 Bonus Challenge: Create a Multi-Page Site!

Want to go further? Create these pages and link them together:

```
index.html (home page)
  ↓
  Contains links to:
  ├─ about.html (about you)
  ├─ hobbies.html (your hobbies)
  └─ contact.html (ways to reach you)
```

**Hint:** Use `<a href="about.html">About Me</a>` to link between your pages!

---

## 🎉 Congratulations!

You just built your first webpage! You're now officially a web developer! 🌐

**Fun Fact:** The first website ever created (in 1991) looked much simpler than what you just made. You're already better than the internet pioneers! 😄

---

**Ready to make it beautiful? Let's go to [Lesson 5: Making It Pretty](lesson05_styling.md)!**

---

*Remember: Every website you visit started as HTML code, just like what you're writing now!*
