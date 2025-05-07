document.addEventListener('DOMContentLoaded', function() {
    // Transform the table into cards
    function transformNoticeTable() {
        const noticeTable = document.querySelector('.table');
        if (!noticeTable) return;
        
        // Create a container for notice cards
        const noticeContainer = document.createElement('div');
        noticeContainer.className = 'notice-container';
        
        // Get all table rows except header
        const rows = noticeTable.querySelectorAll('tbody tr');
        
        // Count the notices
        const noticeCount = rows.length;
        
        // Update the section header with count
        const cardHeader = document.querySelector('.card-header');
        if (cardHeader) {
            cardHeader.innerHTML = `
                <div class="section-header">
                    <h2 class="section-title">
                        <i class="fas fa-bullhorn"></i>
                        Notices <span class="count-badge">${noticeCount}</span>
                    </h2>
                    <a href="#" class="add-notice-btn">
                        <i class="fas fa-plus"></i>
                        Add Notice
                    </a>
                </div>
            `;
        }
        
        // Create a card for each notice
        rows.forEach(row => {
            // Skip empty rows
            if (row.querySelector('.text-center')) return;
            
            // Get cell contents
            const cells = row.querySelectorAll('td');
            if (cells.length < 3) return;
            
            const titleEl = cells[0].querySelector('a');
            const title = titleEl ? titleEl.textContent : cells[0].textContent;
            const link = titleEl ? titleEl.getAttribute('href') : '#';
            const date = cells[1].textContent;
            
            // Create notice card
            const card = document.createElement('div');
            card.className = 'notice-card';
            
            // Create avatar
            const avatar = document.createElement('div');
            avatar.className = 'notice-avatar';
            avatar.textContent = title.charAt(0).toUpperCase();
            
            // Create title
            const titleDiv = document.createElement('div');
            titleDiv.className = 'notice-title';
            titleDiv.textContent = title;
            
            // Create description placeholder
            const descDiv = document.createElement('div');
            descDiv.className = 'notice-description';
            descDiv.textContent = "Don't do this ?";
            
            // Create View More button
            const viewBtn = document.createElement('a');
            viewBtn.className = 'view-more-btn';
            viewBtn.href = link;
            viewBtn.textContent = 'View More';
            
            // Create posted date
            const postedDate = document.createElement('div');
            postedDate.className = 'posted-date';
            postedDate.textContent = `Posted: ${date}`;
            
            // Assemble the card
            card.appendChild(avatar);
            card.appendChild(titleDiv);
            card.appendChild(descDiv);
            card.appendChild(viewBtn);
            card.appendChild(postedDate);
            
            // Add card to container
            noticeContainer.appendChild(card);
        });
        
        // Replace table with cards
        noticeTable.parentNode.replaceChild(noticeContainer, noticeTable);
        
        // Check if there are no notices and create empty state
        if (noticeCount === 0) {
            const emptyState = document.createElement('div');
            emptyState.className = 'empty-state';
            emptyState.innerHTML = `
                <i class="fas fa-clipboard"></i>
                <p>No notices available at the moment.</p>
                <a href="#" class="add-notice-btn">
                    <i class="fas fa-plus"></i> Add Your First Notice
                </a>
            `;
            noticeContainer.appendChild(emptyState);
        }
    }
    
    // Update page header
    function updatePageHeader() {
        const pageTitle = document.querySelector('.page-title');
        if (pageTitle) {
            const notices = document.querySelectorAll('.notice-card');
            const count = notices.length;
            pageTitle.innerHTML = `<i class="fas fa-bullhorn"></i> Notices (${count})`;
        }
    }
    
    // Call the transformation functions
    transformNoticeTable();
    updatePageHeader();
});