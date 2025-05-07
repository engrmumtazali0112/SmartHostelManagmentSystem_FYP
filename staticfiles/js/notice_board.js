document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar functionality
    const toggleSidebar = document.getElementById('toggleSidebar');
    const toggleIcon = document.getElementById('toggleIcon');
    const mainContent = document.getElementById('mainContent');
    let sidebarOpen = true;

    if (toggleSidebar && toggleIcon && mainContent) {
        toggleSidebar.addEventListener('click', function() {
            sidebarOpen = !sidebarOpen;
            if (sidebarOpen) {
                toggleIcon.classList.remove('fa-chevron-right');
                toggleIcon.classList.add('fa-chevron-left');
                mainContent.style.marginLeft = '250px';
                toggleSidebar.style.left = '250px';
            } else {
                toggleIcon.classList.remove('fa-chevron-left');
                toggleIcon.classList.add('fa-chevron-right');
                mainContent.style.marginLeft = '0';
                toggleSidebar.style.left = '0';
            }
        });
    }

    // Transform the table to match the card design in the image
    const transformTable = function() {
        const rows = document.querySelectorAll('.notice-table tbody tr');
        
        rows.forEach(row => {
            const cells = row.querySelectorAll('td');
            if (cells.length >= 5) {
                // Get notice title and date
                const title = cells[0].textContent.trim();
                const date = cells[2].textContent.trim();
                
                // Create a short description element if it doesn't exist
                if (!row.querySelector('.notice-description')) {
                    const descriptionElement = document.createElement('div');
                    descriptionElement.className = 'notice-description';
                    descriptionElement.textContent = "Don't do this ?"; // Default placeholder text
                    
                    // Insert after the title
                    cells[0].insertAdjacentElement('afterend', descriptionElement);
                }
                
                // Create View More button if it doesn't exist
                if (!row.querySelector('.view-more-btn')) {
                    const viewMoreBtn = document.createElement('a');
                    viewMoreBtn.className = 'view-more-btn';
                    viewMoreBtn.href = row.querySelector('.action-btn.view-btn').href;
                    viewMoreBtn.textContent = 'View More';
                    
                    // Insert at the bottom
                    row.appendChild(viewMoreBtn);
                }
                
                // Create posted date element if it doesn't exist
                if (!row.querySelector('.posted-date')) {
                    const postedDateElement = document.createElement('div');
                    postedDateElement.className = 'posted-date';
                    postedDateElement.textContent = `Posted: ${date}`;
                    
                    // Insert at the bottom
                    row.appendChild(postedDateElement);
                }
                
                // Create avatar with first letter if it doesn't exist
                if (!row.querySelector('.notice-avatar')) {
                    const avatarElement = document.createElement('div');
                    avatarElement.className = 'notice-avatar';
                    avatarElement.textContent = title.charAt(0).toUpperCase();
                    
                    // Insert before the title
                    cells[0].insertAdjacentElement('beforebegin', avatarElement);
                }
                
                // Hide action buttons
                const actionButtons = row.querySelector('.action-buttons');
                if (actionButtons) {
                    actionButtons.style.display = 'none';
                }
            }
        });
    };
    
    // Add additional CSS for the new elements
    const addCustomStyles = function() {
        const style = document.createElement('style');
        style.textContent = `
            .notice-table tbody tr {
                display: block;
                position: relative;
                padding: 20px;
                padding-left: 80px;
                margin-bottom: 15px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                background-color: white;
            }
            
            .notice-avatar {
                position: absolute;
                left: 20px;
                top: 20px;
                width: 40px;
                height: 40px;
                background-color: #ff6b6b;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: white;
                font-weight: bold;
            }
            
            .notice-description {
                margin-top: 5px;
                margin-bottom: 30px;
                color: #7f8c8d;
            }
            
            .view-more-btn {
                display: inline-block;
                background-color: #3498db;
                color: white;
                padding: 6px 16px;
                border-radius: 4px;
                text-decoration: none;
                position: absolute;
                left: 80px;
                bottom: 20px;
                font-size: 14px;
            }
            
            .posted-date {
                position: absolute;
                right: 20px;
                bottom: 20px;
                font-size: 14px;
                color: #95a5a6;
            }
            
            .notice-table td {
                padding: 0;
                border: none;
            }
            
            .notice-table td:first-child {
                font-weight: bold;
                font-size: 18px;
                padding-top: 0;
                padding-left: 0;
            }
        `;
        document.head.appendChild(style);
    };
    
    // Call the functions to transform the table
    setTimeout(() => {
        addCustomStyles();
        transformTable();
    }, 100);
});