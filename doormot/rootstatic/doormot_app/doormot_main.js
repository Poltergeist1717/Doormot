function toggleSideMenu() {
    const sideMenu = document.getElementById('side-menu');
    const content = document.getElementById('content');
    const hamburger = document.getElementById('hamburger');

    if (sideMenu.style.width === '0px' || sideMenu.style.width === '') {
        sideMenu.style.width = '250px';
        content.style.marginLeft = '250px';
        hamburger.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
        `;
    } else {
        sideMenu.style.width = '0';
        content.style.marginLeft = '0';
        hamburger.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
        `;
    }
}

const rentSwitchButton = document.getElementById('rent-switch')
const buySwitchButton = document.getElementById('buy-switch')
const sellSwitchButton = document.getElementById('sell-switch')

function switchRentBuySell() {
    if rentSwitchButton.style.display = 
}