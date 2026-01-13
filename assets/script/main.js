// // Sample data for past papers (this will come from your Django backend)
// const samplePapers = [
//     {
//         id: 1,
//         title: "Mathematics Paper 2",
//         subject: "Mathematics",
//         level: "O-Level",
//         year: 2023,
//         type: "Main Exam",
//         downloads: 1542,
//         fileSize: "2.4 MB"
//     },
//     {
//         id: 2,
//         title: "Physics Paper 1",
//         subject: "Physics",
//         level: "A-Level",
//         year: 2023,
//         type: "Main Exam",
//         downloads: 987,
//         fileSize: "1.8 MB"
//     },
//     {
//         id: 3,
//         title: "Chemistry Practical",
//         subject: "Chemistry",
//         level: "O-Level",
//         year: 2022,
//         type: "Practical",
//         downloads: 765,
//         fileSize: "3.2 MB"
//     },
//     {
//         id: 4,
//         title: "Biology Theory",
//         subject: "Biology",
//         level: "A-Level",
//         year: 2022,
//         type: "Theory",
//         downloads: 543,
//         fileSize: "2.1 MB"
//     }
// ];

// // DOM Content Loaded
// document.addEventListener('DOMContentLoaded', function() {
//     loadPapers();
//     setupEventListeners();
// });

// // Load papers into the grid
// function loadPapers() {
//     const papersGrid = document.getElementById('papersGrid');
//     papersGrid.innerHTML = '';

//     samplePapers.forEach(paper => {
//         const paperCard = createPaperCard(paper);
//         papersGrid.appendChild(paperCard);
//     });
// }

// // Create paper card HTML
// function createPaperCard(paper) {
//     const card = document.createElement('div');
//     card.className = 'paper-card';
//     card.innerHTML = `
//         <div class="paper-header">
//             <span class="paper-badge">${paper.level}</span>
//             <span class="paper-year">${paper.year}</span>
//         </div>
//         <h3 class="paper-title">${paper.title}</h3>
//         <div class="paper-meta">
//             <span><i class="fas fa-book"></i> ${paper.subject}</span>
//             <span><i class="fas fa-download"></i> ${paper.downloads}</span>
//         </div>
//         <div class="paper-meta">
//             <span><i class="fas fa-file-pdf"></i> ${paper.fileSize}</span>
//             <span><i class="fas fa-calendar"></i> ${paper.type}</span>
//         </div>
//         <button class="btn btn-primary paper-download" onclick="downloadPaper(${paper.id})">
//             <i class="fas fa-download"></i>
//             Download Paper
//         </button>
//     `;
//     return card;
// }

// // Setup event listeners
// function setupEventListeners() {
//     // Load more button
//     const loadMoreBtn = document.getElementById('loadMoreBtn');
//     if (loadMoreBtn) {
//         loadMoreBtn.addEventListener('click', loadMorePapers);
//     }

//     // Mobile menu toggle
//     const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
//     const navLinks = document.querySelector('.nav-links');

//     if (mobileMenuBtn && navLinks) {
//         mobileMenuBtn.addEventListener('click', function() {
//             navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
//         });
//     }

//     // Smooth scrolling for navigation links
//     document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//         anchor.addEventListener('click', function (e) {
//             e.preventDefault();
//             const target = document.querySelector(this.getAttribute('href'));
//             if (target) {
//                 target.scrollIntoView({
//                     behavior: 'smooth',
//                     block: 'start'
//                 });
//             }
//         });
//     });

//     // Search functionality
//     const searchInput = document.querySelector('.search-input');
//     if (searchInput) {
//         searchInput.addEventListener('input', function(e) {
//             const searchTerm = e.target.value.toLowerCase();
//             filterPapers(searchTerm);
//         });
//     }

//     // Filter functionality
//     const filterBtn = document.querySelector('.filter-btn');
//     if (filterBtn) {
//         filterBtn.addEventListener('click', applyFilters);
//     }
// }

// // Filter papers based on search term
// function filterPapers(searchTerm) {
//     const filteredPapers = samplePapers.filter(paper =>
//         paper.title.toLowerCase().includes(searchTerm) ||
//         paper.subject.toLowerCase().includes(searchTerm) ||
//         paper.level.toLowerCase().includes(searchTerm) ||
//         paper.year.toString().includes(searchTerm)
//     );

//     displayFilteredPapers(filteredPapers);
// }

// // Apply advanced filters
// function applyFilters() {
//     const levelFilter = document.querySelector('.filter-select:nth-child(1)').value;
//     const subjectFilter = document.querySelector('.filter-select:nth-child(2)').value;
//     const yearFilter = document.querySelector('.filter-select:nth-child(3)').value;

//     let filteredPapers = samplePapers;

//     if (levelFilter) {
//         filteredPapers = filteredPapers.filter(paper =>
//             paper.level.toLowerCase() === levelFilter.toLowerCase()
//         );
//     }

//     if (subjectFilter) {
//         filteredPapers = filteredPapers.filter(paper =>
//             paper.subject.toLowerCase() === subjectFilter.toLowerCase()
//         );
//     }

//     if (yearFilter) {
//         filteredPapers = filteredPapers.filter(paper =>
//             paper.year.toString() === yearFilter
//         );
//     }

//     displayFilteredPapers(filteredPapers);
// }

// // Display filtered papers
// function displayFilteredPapers(papers) {
//     const papersGrid = document.getElementById('papersGrid');
//     papersGrid.innerHTML = '';

//     if (papers.length === 0) {
//         papersGrid.innerHTML = `
//             <div class="no-results" style="grid-column: 1/-1; text-align: center; padding: 2rem;">
//                 <i class="fas fa-search" style="font-size: 3rem; color: #6b7280; margin-bottom: 1rem;"></i>
//                 <h3>No papers found</h3>
//                 <p>Try adjusting your search or filters</p>
//             </div>
//         `;
//         return;
//     }

//     papers.forEach(paper => {
//         const paperCard = createPaperCard(paper);
//         papersGrid.appendChild(paperCard);
//     });
// }

// // Load more papers (simulated)
// function loadMorePapers() {
//     // In a real app, this would fetch more data from the server
//     const loadMoreBtn = document.getElementById('loadMoreBtn');
//     loadMoreBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
//     loadMoreBtn.disabled = true;

//     setTimeout(() => {
//         // Simulate adding more papers
//         const newPapers = [
//             {
//                 id: 5,
//                 title: "English Language",
//                 subject: "English",
//                 level: "O-Level",
//                 year: 2023,
//                 type: "Main Exam",
//                 downloads: 432,
//                 fileSize: "1.5 MB"
//             },
//             {
//                 id: 6,
//                 title: "Additional Mathematics",
//                 subject: "Mathematics",
//                 level: "A-Level",
//                 year: 2022,
//                 type: "Theory",
//                 downloads: 321,
//                 fileSize: "2.8 MB"
//             }
//         ];

//         newPapers.forEach(paper => {
//             samplePapers.push(paper);
//             const paperCard = createPaperCard(paper);
//             document.getElementById('papersGrid').appendChild(paperCard);
//         });

//         loadMoreBtn.innerHTML = '<i class="fas fa-plus"></i> Load More Papers';
//         loadMoreBtn.disabled = false;
//     }, 1000);
// }

// // Download paper function
// function downloadPaper(paperId) {
//     // In a real app, this would trigger a download from your Django backend
//     const paper = samplePapers.find(p => p.id === paperId);
//     if (paper) {
//         alert(`Downloading: ${paper.title} (${paper.year})`);
//         // Simulate download
//         paper.downloads++;

//         // Update the download count display
//         const downloadSpan = document.querySelector(`[onclick="downloadPaper(${paperId})"]`)
//                             ?.closest('.paper-card')
//                             ?.querySelector('.fa-download')
//                             ?.closest('span');
//         if (downloadSpan) {
//             downloadSpan.textContent = ` ${paper.downloads}`;
//         }
//     }
// }

// // Initialize filters
// function initializeFilters() {
//     // This would be populated from your Django backend in a real app
//     console.log('Filters initialized');
// }
