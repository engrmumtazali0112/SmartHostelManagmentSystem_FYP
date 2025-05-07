// Notice detail page enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Check if notice is about to expire and add visual indicator
    const expiryBadge = document.querySelector('.expiry-date');
    if (expiryBadge) {
        const expiryDate = new Date(expiryBadge.textContent.replace('Expires: ', ''));
        const today = new Date();
        const daysUntilExpiry = Math.ceil((expiryDate - today) / (1000 * 60 * 60 * 24));
        
        if (daysUntilExpiry <= 7 && daysUntilExpiry > 0) {
            expiryBadge.style.background = '#ff9800';
            expiryBadge.style.color = 'white';
            expiryBadge.innerHTML += ` <span class="expiry-warning">(${daysUntilExpiry} days left)</span>`;
        } else if (daysUntilExpiry <= 0) {
            expiryBadge.style.background = '#f44336';
            expiryBadge.style.color = 'white';
            expiryBadge.innerHTML += ' <span class="expiry-warning">(Expired)</span>';
        }
    }
    
    // Add animation for attachments
    const attachments = document.querySelectorAll('.attachment-item');
    if (attachments.length > 0) {
        attachments.forEach((attachment, index) => {
            attachment.style.animationDelay = `${index * 0.1}s`;
            attachment.classList.add('animated-attachment');
        });
    }
    
    // Add progress tracker for long notices
    const noticeContent = document.querySelector('.notice-content');
    if (noticeContent && noticeContent.offsetHeight > 500) {
        const progressContainer = document.createElement('div');
        progressContainer.className = 'reading-progress-container';
        progressContainer.innerHTML = '<div class="reading-progress-bar"></div>';
        
        document.querySelector('.notice-card').prepend(progressContainer);
        
        window.addEventListener('scroll', function() {
            const totalHeight = noticeContent.offsetHeight;
            const scrollPosition = window.scrollY - noticeContent.offsetTop + window.innerHeight / 2;
            const scrollPercentage = Math.min(100, Math.max(0, (scrollPosition / totalHeight) * 100));
            
            document.querySelector('.reading-progress-bar').style.width = `${scrollPercentage}%`;
        });
    }
    
    // Add highlight functionality for text selection
    noticeContent.addEventListener('mouseup', function() {
        const selection = window.getSelection();
        if (selection.toString().length > 0) {
            // Create highlight button if it doesn't exist
            if (!document.querySelector('.highlight-btn')) {
                const highlightBtn = document.createElement('button');
                highlightBtn.className = 'highlight-btn';
                highlightBtn.innerHTML = '<i class="fas fa-highlighter"></i>';
                document.body.appendChild(highlightBtn);
                
                highlightBtn.addEventListener('click', function() {
                    const range = selection.getRangeAt(0);
                    const span = document.createElement('span');
                    span.className = 'highlighted-text';
                    range.surroundContents(span);
                    highlightBtn.remove();
                });
            }
            
            // Position the button near the selection
            const selectionRect = selection.getRangeAt(0).getBoundingClientRect();
            const highlightBtn = document.querySelector('.highlight-btn');
            highlightBtn.style.top = `${window.scrollY + selectionRect.top - 30}px`;
            highlightBtn.style.left = `${window.scrollX + selectionRect.left + selectionRect.width / 2}px`;
            highlightBtn.style.display = 'block';
        } else {
            const highlightBtn = document.querySelector('.highlight-btn');
            if (highlightBtn) {
                highlightBtn.style.display = 'none';
            }
        }
    });
    
    // Add animation when page loads
    document.querySelector('.notice-card').classList.add('fade-in-up');
});