document.addEventListener('DOMContentLoaded', function() {
    // Load CSV data for the cards
    loadCSVData('best 30.csv', 'best30-cards');
    loadCSVData('new 15.csv', 'new15-cards');

    // Load rating data and update titles
    loadRatingData('rating.csv');
});

function loadCSVData(csvFile, containerId) {
    fetch(csvFile)
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n').slice(1); // Skip header row
            const container = document.getElementById(containerId);
            rows.forEach(row => {
                if (row === '') return; // Skip empty rows
                const cols = row.split(',');
                const level = cols[1].trim().toLowerCase(); // Get the level
                const musicNameColorClass = getMusicNameColorClass(level);

                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <h3 class="${musicNameColorClass}">${cols[0].trim()}</h3>
                    <p>${cols[2].trim()} | ${cols[3].trim()}</p> <!-- Tech Score | Rank -->
                    <p>${cols[4].trim()} → ${cols[5].trim()}</p> <!-- Difficulty → Rating -->
                `;
                container.appendChild(card);
                console.log(cols[0].trim());
            });
        })
        .catch(error => console.error('Error loading CSV file:', error));
}

function loadRatingData(csvFile) {
    fetch(csvFile)
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n').slice(1); // Skip header row
            const cols = rows[0].split(','); // Assuming only one row

            // Update the titles with the rating averages
            document.querySelector('h1').textContent += ` (b45: ${cols[2].trim()})`;
            document.querySelectorAll('h2')[0].textContent += ` (${cols[0].trim()})`;
            document.querySelectorAll('h2')[1].textContent += ` (${cols[1].trim()})`;
        })
        .catch(error => console.error('Error loading rating CSV file:', error));
}

function getMusicNameColorClass(level) {
    switch(level) {
        case 'basic':
            return 'level-basic';
        case 'advanced':
            return 'level-advanced';
        case 'expert':
            return 'level-expert';
        case 'master':
            return 'level-master';
        case 'lunatic':
            return 'level-lunatic';
        default:
            return '';
    }
}
