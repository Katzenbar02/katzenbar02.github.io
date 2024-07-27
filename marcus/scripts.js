// scripts.js
let currentPostIndex = 0;

document.addEventListener('DOMContentLoaded', function() {
    fetchLinkedInPosts();
    updatePostsVisibility();
    handleScroll();
    window.addEventListener('scroll', handleScroll);
});

function fetchLinkedInPosts() {
    // Mock data to illustrate
    const posts = [
        {
            title: "Understanding the Importance of Employee Training",
            content: "Employee training is a vital part of any business. It helps employees acquire new skills, improves performance, and increases job satisfaction.",
            link: "https://www.linkedin.com/in/marcus-ludwig1/detail/recent-activity/",
            image: "path/to/image1.jpg"
        },
        {
            title: "Effective HR Policy Development",
            content: "Creating effective HR policies is crucial for maintaining a productive and positive work environment.",
            link: "https://www.linkedin.com/in/marcus-ludwig1/detail/recent-activity/",
            image: "path/to/image2.jpg"
        }
    ];

    const container = document.getElementById('linkedin-posts');
    posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.classList.add('post');
        postElement.innerHTML = `
            <img src="${post.image}" alt="${post.title}">
            <h3>${post.title}</h3>
            <p>${post.content}</p>
            <a href="${post.link}" target="_blank">Read more</a>
        `;
        container.appendChild(postElement);
    });

    updatePostsVisibility();
}

function updatePostsVisibility() {
    const posts = document.querySelectorAll('.post');
    posts.forEach((post, index) => {
        post.classList.toggle('active', index === currentPostIndex);
    });
}

function prevPost() {
    const posts = document.querySelectorAll('.post');
    currentPostIndex = (currentPostIndex - 1 + posts.length) % posts.length;
    updatePostsVisibility();
}

function nextPost() {
    const posts = document.querySelectorAll('.post');
    currentPostIndex = (currentPostIndex + 1) % posts.length;
    updatePostsVisibility();
}

function handleScroll() {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}
