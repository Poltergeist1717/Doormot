
function updateUserTypeAndSubmit(){
    var selectedUserType = document.getElementById("userTypeSelect").value;
    document.getElementById("userTypeInput").value = selectedUserType;
    return true;
    
}

// function updateUserTypeInSecondForm(){
//     var selectedUserType = updateUserTypeAndSubmit();
//     document.getElementById('userTypeInput').value = selectedUserType;
//     return true;
// }





// To Diplay Filter Search Box - 
// To allow user interract with options to filter search  
function displayFilteredSearchBox() {
    var filter_box = document.getElementById('filter-choices-box');

    if (filter_box.style.display === 'none' || filter_box.style.display === '') {
        filter_box.style.display = 'block';

    } else {
        filter_box.style.display = 'none';
    }

}

function hideFilteredPropBox() {
    var filter_treat = document.getElementById('property-box');

    if (window.innerWidth <= 768) {
        if (filter_treat.style.display === 'block' || filter_treat.style.display === ''){
            filter_treat.style.display = 'none';
        } else {
            filter_treat.style.display = 'block';
        }

        }
        
}

document.getElementById('filter-icon').addEventListener('click', function(){
    displayFilteredSearchBox();
    hideFilteredPropBox();
});




// To Diplay Filter Search Box - 
// To allow user interract with options to filter search  
function displayFilteredSearchBox2() {
    var filter_box = document.getElementById('filter-choices-box2');

    if (filter_box.style.display === 'none' || filter_box.style.display === '') {
        filter_box.style.display = 'block';
      
    } else {
        filter_box.style.display = 'none';
    }

}



function hideFilteredPropBox2() {
    var filter_treat = document.getElementById('filtered_property_box2');

    if (window.innerWidth <= 768) {
        if (filter_treat.style.display === 'block' || filter_treat.style.display === ''){
            filter_treat.style.display = 'none';
        } else {
            filter_treat.style.display = 'block';
        }

        }
        
}

document.getElementById('filter-icon').addEventListener('click', function(){
    displayFilteredSearchBox2();
    hideFilteredPropBox2();
});



// To Diplay Filter Search Box - 
// To allow user interract with options to filter search  
function displayPropertyDetailsOverlay(propertyID) {
    var property_details_overlay_box = document.getElementById('property-details-overlay-'+propertyID);

    if (property_details_overlay_box.style.display === 'none' || property_details_overlay_box.style.display === '') {
        property_details_overlay_box.style.opacity = '0';
        property_details_overlay_box.style.display = 'block';
        
        property_details_overlay_box.offsetHeight;

        property_details_overlay_box.style.transition = 'opacity 0.6s ease-in-out';
        property_details_overlay_box.style.opacity = '1';
    }

}
var property_display_box = document.getElementById('property-display-box');
property_display_box.addEventListener('mouseover', displayPropertyDetailsOverlay);


function hidePropertyDetailsOverlay(propertyID) {
    var hide_property_details_overlay_box = document.getElementById('property-details-overlay-'+propertyID);

    if (hide_property_details_overlay_box.style.display === 'block') {
        hide_property_details_overlay_box.style.display = 'none';
    } else {
        hide_property_details_overlay_box.style.display = 'none';
    }

}

var overlay_hide = document.getElementById('overlay-hider');
overlay_hide.addEventListener('mouseout', hidePropertyDetailsOverlay);


// To Diplay Filter Search buttton Icon Label - 
// Enables user to know what the button icon is for 
function displayFilterName() {
    var filter_name = document.getElementById('filter-name');

    if (filter_name.style.display === 'none' || filter_name.style.display === '') {
        filter_name.style.display = 'flex';
    } else {
        filter_name.style.display = 'none';
    }

}
var filter_icon = document.getElementById('filter-icon');
filter_icon.addEventListener('onmouseover', displayFilterName);



// To Diplay Upload Property buttton Icon Label - 
// Enables user to know what the button icon is for 
function displayUploadPropertyLabel() {
    var upload_property_name = document.getElementById('upload-property-label');

    if (upload_property_name.style.display === 'none' || upload_property_name.style.display === '') {
        upload_property_name.style.display = 'flex';
    } else {
        upload_property_name.style.display = 'none';
    }

}
var upload_property_icon = document.getElementById('upload-property-label');
upload_property_icon.addEventListener('onmouseover', displayUploadPropertyLabel);


// To change Book Mark Icon - 
// To show user has bookmarked 
function changeBookMarkIcon(propertyID) {
    
    var book_mark_icon = document.getElementById('book-mark-'+propertyID);

    if (book_mark_icon.innerHTML === `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
    <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
</svg>`)
    {
        book_mark_icon.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" fill="white" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
    </svg>`;
    } else {
        book_mark_icon.innerHTML =`<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z" />
    </svg>`;
    }

}
var book_mark_icon = document.getElementById('book-mark');
filter_icon.addEventListener('click', changeBookMarkIcon);



// To display commercial property sub-choices - 
// Enables user to choose sub-choice for commercial property 

function showQuestMoreInfo(elementID){
    var show_variable = document.getElementById(elementID);  
    if (show_variable.style.display === 'none' || show_variable.style.display === ''){
        show_variable.style.display = 'block';
    }
}

function hideQuestMoreInfo(elementID){
    var hide_variable = document.getElementById(elementID); 
    if (hide_variable.style.display === 'block' || hide_variable.style.display === ''){
        hide_variable.style.display = 'none';
    } else {
        hide_variable.style.display = 'none';
    }
}


// Functions to handle Showing More Info about Commercial Building Type Of Property
function showComSubBuildMoreInfo(elementIDs){
    console.log('elementIDs:', elementIDs);
    for (let elementID of elementIDs){
        console.log('elementID:', elementID);
        let show_currentVar = document.getElementById(elementID);
        if (show_currentVar.style.display === 'none' || show_currentVar.style.display === ''){
            show_currentVar.style.display = 'block';
        } else {
            // No action needed
        }
    }
}

// Functions to handle Hiding More Info about Commercial Building Type Of Property
function hideComSubBuildMoreInfo(elementIDs){
    console.log('elementIDs:', elementIDs);
    for (let elementID of elementIDs){
        console.log('elementID:', elementID);
        let hide_currentVar = document.getElementById(elementID);
        if (hide_currentVar.style.display === 'block' || hide_currentVar.style.display === ''){
            hide_currentVar.style.display = 'none';
        } else {
            hide_currentVar.style.display = 'none';
        }
    }
}


// Functions to handle Showing More Info about Type Of Property
function showTypeOfPropMoreInfo(elementIDs){
    console.log('elementIDs:', elementIDs);
    for (let elementID of elementIDs){
        console.log('elementID:', elementID);
        let show_currentVar = document.getElementById(elementID);
        if (show_currentVar.style.display === 'none' || show_currentVar.style.display === ''){
            show_currentVar.style.display = 'block';
        } else {
            // No action needed
        }
    }
}

// Functions to handle Hiding More Info about Type Of Property
function hideTypeOfPropMoreInfo(elementIDs){
    console.log('elementIDs:', elementIDs);
    for (let elementID of elementIDs){
        console.log('elementID:', elementID);
        let hide_currentVar = document.getElementById(elementID);
        if (hide_currentVar.style.display === 'block' || hide_currentVar.style.display === ''){
            hide_currentVar.style.display = 'none';
        } else {
            hide_currentVar.style.display = 'none';
        }
    }
}



var for_sale = document.getElementById('for_sale')
for_sale.addEventListener('onclick', SubmitEvent)





document.addEventListener("DOMContentLoaded", function() {
    const lazyImages = document.querySelectorAll('.lazy-image');

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                observer.unobserve(img);
            }
        });
    });

    lazyImages.forEach(image => {
        observer.observe(image);
    });
});


// To Diplay Filter Search Box - 
// To allow user interract with options to filter search  
function displayFilterPropertyUsernameForm() {
    var filter_property = document.getElementById('filterPropertyUsernameFormDiv');
    var filter_property_form_button = document.getElementById('filterPropertyUsernameFormButton');

    if (filter_property.style.display === 'none' || filter_property.style.display === '') {
        filter_property.style.display = 'block';
        filter_property_form_button.innerHTML = `<p>Filter properties with username</p> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="#ffffff" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 19V6M5 12l7-7 7 7"/>
      </svg>`;
      
    } else {
        filter_property.style.display = 'none';
        filter_property_form_button.innerHTML = `<p>Filter properties with username</p> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="#ffffff" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 5v13M5 12l7 7 7-7"/>
    </svg>`;
    }

}

var filter_property_form_button = document.getElementById('filterPropertyUsernameFormButton')
filter_property_form_button.addEventListener('onclick', displayFilterPropertyUsernameForm)


let isSliderPaused = false;
const sliderContainer = document.getElementById('slider-container');
const slider = document.getElementById('slider');

function startSlider() {
            isSliderPaused = false;
            moveSlider();
        }

function pauseSlider() {
            isSliderPaused = true;
        }

function moveSlider() {
    if (!isSliderPaused) {
        const firstSlide = slider.children[0];
        slider.appendChild(firstSlide.cloneNode(true));
        slider.style.transform = 'translateX(-100%)';
        setTimeout(() => {
            slider.style.transition = 'none';
            slider.style.transform = 'translateX(0)';
            setTimeout(() => {
                slider.style.transition = 'transform 0.5s ease-in-out';
                slider.removeChild(firstSlide);
                moveSlider();
                    }, 0);
                }, 500);
            }
        }

        sliderContainer.addEventListener('focus', startSlider);
        sliderContainer.addEventListener('blur', pauseSlider);

        // Start the slider initially
        startSlider();

// All States

const nigeriaStatesData = [
    {
      "state": "Abia",
      "senatorial_districts": [
        "Abia Central", 
        "Abia North", 
        "Abia South"
      ],
      "lgas": [
        "Aba North",
        "Arochukwu",
        "Aba South",
        "Isiala Ngwa South",
        "Bende",
        "Ikwuano",
        "Isiala",
        "Ngwa North",
        "Isukwuato",
        "Ukwa West",
        "Ukwa East",
        "Umuahia South",
        "Umuahia"
      ]
    },
    {
      "state": "Adamawa",
      "senatorial_districts": [
        "Adamawa Central",
        "Adamawa North",
        "Adamawa South"
      ],
      "lgas": [
        "Demsa",
        "Fufore",
        "Ganye",
        "Girei",
        "Gombi",
        "Jada",
        "Yola North",
        "Lamurde",
        "Madagali",
        "Maiha",
        "Mayo-Belwa",
        "Michika",
        "Mubi South",
        "Numna",
        "Shelleng",
        "Song",
        "Toungo",
        "Jimeta",
        "Yola South",
        "Hung"
      ]
    },
    {
      "state": "Akwa Ibom",
      "senatorial_districts": [
        "Akwa Ibom North East",
        "Akwa Ibom North West",
        "Akwa Ibom South"
      ],
      "lgas": [
        "Abak",
        "Eastern Obolo",
        "Eket",
        "Essien Udim",
        "Etimekpo",
        "Etinan",
        "Ibeno",
        "Ibesikpo Asutan",
        "Ibiono Ibom",
        "Ika",
        "Ikono",
        "Ikot Abasi",
        "Ikot Ekpene",
        "Ini",
        "Itu",
        "Mbo",
        "Mkpat Enin",
        "Nsit Ibom",
        "Nsit Ubium",
        "Obot Akara",
        "Okobo",
        "Onna",
        "Orukanam",
        "Oron",
        "Udung Uko",
        "Ukanafun",
        "Esit Eket",
        "Uruan",
        "Urue Offoung",
        "Oruko Ete",
        "Uyo"
      ]
    },
    {
      "state": "Anambra",
      "senatorial_districts": [
        "Anambra Central",
        "Anambra North",
        "Anambra South"
      ],
      "lgas": [
        "Aguata",
        "Akwa North",
        "Anambra",
        "Anambra-West",
        "Anaocha",
        "Awka-North",
        "Awka-South",
        "Ayamelum",
        "Dunukofia",
        "Ekwusigo",
        "Idemili-North",
        "Idemili-South",
        "Ihiala",
        "Imo",
        "Nibo",
        "Njikoka",
        "Nnewi-North",
        "Nnewi-South",
        "Ogbaru",
        "Olumba",
        "Onitsha-North",
        "Onitsha-South",
        "Orumba-North",
        "Orumba-South",
        "Oti",
        "Otu-Ocha",
        "Ubuluizor Ihiala",
        "Uyi"
      ]
    },
    {
      "state": "Bauchi",
      "senatorial_districts": [
        "Bauchi Central",
        "Bauchi North",
        "Bauchi South"
      ],
      "lgas": [
        "Alkaleri",
        "Bauchi",
        "Bogoro",
        "Damban",
        "Darazo",
        "Dass",
        "Gamawa",
        "Ganjuwa",
        "Giade",
        "Itas\/Gadau",
        "Jama'Are",
        "Katagum",
        "Kirfi",
        "Misau",
        "Ningi",
        "Shira",
        "Tafawa-Balewa",
        "Toro",
        "Warji",
        "Zaki"
      ]
    },
    {
      "state": "Benue",
      "senatorial_districts": [
        "Benue North East",
        "Benue North West",
        "Benue South"
      ],
      "lgas": [
        "Ado",
        "Agatu",
        "Apa",
        "Buruku",
        "Gboko",
        "Guma",
        "Gwer-East",
        "Gwer-West",
        "Katsina-Ala",
        "Konshisha",
        "Kwande",
        "Logo",
        "Makurdi",
        "Ogbadibo",
        "Ohimini",
        "Oju",
        "Okpokwu",
        "Otukpo",
        "Oturkpa",
        "Tarka",
        "Ukum",
        "Vandekya"
      ]
    },
    {
      "state": "Borno",
      "senatorial_districts": [
        "Borno Central",
        "Borno North",
        "Borno South"
      ],
      "lgas": [
        "Abadan",
        "Askira-Uba",
        "Bama",
        "Bayo",
        "Biu",
        "Chibok",
        "Damboa",
        "Dikwa",
        "Gubio",
        "Guzamala",
        "Gwoza",
        "Hawul",
        "Jere",
        "Kaga",
        "Kala\/Balge",
        "Konduga",
        "Kukawa",
        "Kwaya-Kusar",
        "Mafa",
        "Magumeri",
        "Maiduguri",
        "Marte",
        "Mobbar",
        "Mongunu",
        "Ngala",
        "Nganzai",
        "Shani"
      ]
    },
    {
      "state": "Bayelsa",
      "senatorial_districts": [
        "Bayelsa Central",
        "Bayelsa East",
        "Bayelsa West"
        ],
      "lgas": [
        "Adagbabiri",
        "Brass",
        "Ekeremor",
        "Kembe",
        "Kolokuma",
        "Kolokuma\/Opkuma",
        "Nembe",
        "Ogbia",
        "Sagbama",
        "Southern-Ijaw",
        "Toru-Abubo",
        "Yenegoa"
      ]
    },
    {
      "state": "Cross River",
      "senatorial_districts": [
        "Cross River Central",
        "Cross River North",
        "Cross River South"
      ],
      "lgas": [
        "Abi",
        "Abuochichie",
        "Akamkpa",
        "Akpabuyo",
        "Bakassi",
        "Bekwara",
        "Biasi",
        "Boki",
        "Calabar-Municipal",
        "Calabar-South",
        "Etunk",
        "Ikom",
        "Obanliku",
        "Obubra",
        "Obudu",
        "Odukpani",
        "Ogoja",
        "Ugep-North",
        "Yakurr",
        "Yala"
      ]
    },
    {
      "state": "Delta",
      "senatorial_districts": [
        "Delta Central",
        "Delta North",
        "Delta South"
      ],
      "lgas": [
        "Aniocha North",
        "Aniocha-North",
        "Aniocha-South",
        "Bomadi",
        "Burutu",
        "Effurun",
        "Ethiope-East",
        "Ethiope-West",
        "Idu",
        "Ika-Ne",
        "Ika-North-East",
        "Ika-South",
        "Ikpemili",
        "Isoko-North",
        "Isoko-South",
        "Ndokwa-East",
        "Ndokwa-North",
        "Ndokwa-South",
        "Ndokwa-West",
        "Okpe",
        "Okwuani",
        "Oleh",
        "Oshielli-North",
        "Oshimili",
        "Oshimili-North",
        "Oshimili-South",
        "Osimili",
        "Osimili-North",
        "Osimili-South",
        "Patani",
        "Sapele",
        "Udokwa",
        "Udu",
        "Ughelli-North",
        "Ughelli-South",
        "Ukwuani",
        "Uraun",
        "Urwie",
        "Uvie",
        "Uvwei",
        "Uvwie",
        "Uwvie",
        "Warri-Central",
        "Warri-North",
        "Warri-South"
      ]
    },
    {
      "state": "Ebonyi",
      "senatorial_districts": [
        "Ebonyi South",
        "Ebonyi Central",
        "Ebonyi North"
      ],
      "lgas": [
        "Abakaliki",
        "Afikpo-North",
        "Afikpo-South",
        "Bomadim",
        "Ebonyi",
        "Ezza-North",
        "Ezza-South",
        "Ikwo",
        "Ishielu",
        "Ivo",
        "Izzi",
        "Obaukwu",
        "Ohakwu",
        "Onicha",
        "Ukaba"
      ]
    },
    {
      "state": "Edo",
      "senatorial_districts": [
        "Edo South",
        "Edo Central",
        "Edo North"
      ],
      "lgas": [
        "Afokpella",
        "Afuze",
        "Agbazilo",
        "Akoko Edo",
        "Akoko-Edo",
        "Egor",
        "Esan-Central",
        "Esan-North-East",
        "Esan-North-East",
        "Esan-South-East",
        "Esan-West",
        "Etsako-Central",
        "Etsako-East",
        "Etsako-West",
        "Igueben",
        "Iguobano North East",
        "Ikpoba-Okha",
        "Ohunmwode",
        "Ologbo",
        "Opoji Irrua",
        "Opoji Irrua",
        "Oredo",
        "Orhionmwon",
        "Ovia-North-East",
        "Ovia-South-West",
        "Owan East",
        "Owan-East",
        "Owan-West",
        "Uhunmwonde"
      ]
    },
    {
      "state": "Ekiti",
      "senatorial_districts": [
        "Ekiti South",
        "Ekiti Central",
        "Ekiti North"
      ],
      "lgas": [
        "Ado-Ekiti",
        "Aiyekire",
        "Efon",
        "Ekiti-East",
        "Ekiti-South-West",
        "Ekiti-West",
        "Emure\/Ise\/Orun",
        "Gbonyin",
        "Ido-Osi",
        "Ijero",
        "Ikare",
        "Ikere",
        "Ikole",
        "Ilejemeje",
        "Irepodun\/Ifelodun",
        "Ise-Orun",
        "Moba",
        "Oye"
      ]
    },
    {
      "state": "Enugu",
      "senatorial_districts": [
        "Enugu North",
        "Enugu East",
        "Enugu West"
      ],
      "lgas": [
        "Aninri",
        "Awgu",
        "Enugu-East",
        "Enugu-North",
        "Enugu-South",
        "Ezeagu",
        "Igbo-Etiti",
        "Igbo-Eze-North",
        "Igbo-Eze-South",
        "Isi-Uzo",
        "Nkanu-East",
        "Nkanu-West",
        "Nsukka",
        "Nukanu East",
        "Oji-River",
        "Udenu",
        "Udi",
        "Uzo-Uwani"
      ]
    },
    {
      "state": "Federal Capital Territory",
      "senatorial_districts": [
        "Federal Capital Territory"
      ],
      "lgas": [
        "Abaji",
        "Abuja Municipal",
        "Gwagwalada",
        "Kuje",
        "Bwari",
        "Kwali"
      ]
    },
    {
      "state": "Gombe",
      "senatorial_districts": [
        "Gombe Central",
        "Gombe North",
        "Gombe South"
      ],
      "lgas": [
        "Akko",
        "Balanga",
        "Billiri",
        "Dukku",
        "Funakaye",
        "Gombe",
        "Kaltungo",
        "Kwami",
        "Nafada\/Bajoga",
        "Shomgom",
        "Yamaltu\/Deba"
      ]
    },
    {
      "state": "Imo",
      "senatorial_districts": [
        "Imo East",
        "Imo North",
        "Imo West"
      ],
      "lgas": [
        "Aboh-Mbaise",
        "Ahiazu-Mbaise",
        "Dral-Esat",
        "Ehime-Mbano",
        "Ezeobodo",
        "Ezinihitte",
        "Ideato",
        "Ideato-North",
        "Ideato-South",
        "Ihitte\/Uboma",
        "Ikeduru",
        "Isiala-Mbano",
        "Isu",
        "Mbaitoli",
        "Mbano",
        "Ngor-Okpala",
        "Njaba",
        "Nkwerre",
        "Nwangele",
        "Obowo",
        "Oguta",
        "Ohaji-Egbema",
        "Okigwe",
        "Onuimo",
        "Orlu",
        "Oro-West",
        "Orsu",
        "Oru-East",
        "Oru-West",
        "Owerri-Municipal",
        "Owerri-North",
        "Owerri-West",
        "Ugiri-Ike Ikeduru",
        "Ugiri-Ikedikeduru",
        "Unbano",
        "Zinihitte"
      ]
    },
    {
      "state": "Jigawa",
      "senatorial_districts": [
        "Jigawa North - West",
        "Jigawa North – East",
        "Jigawa South – West"
      ],
      "lgas": [
        "Auyo",
        "Babura",
        "Biriniwa",
        "Birnin-Kudu",
        "Bosuwa",
        "Buji",
        "Dutse",
        "Gagarawa",
        "Garki",
        "Gumel",
        "Guri",
        "Gwaram",
        "Gwiwa",
        "Hadejia",
        "Jahun",
        "Kafin-Hausa",
        "Kaugama",
        "Kazaure",
        "Kirkasamma",
        "Maigatari",
        "Malam-Maduri",
        "Miga",
        "Ringim",
        "Roni",
        "Sule-Tankarkar",
        "Taura",
        "Yankwashi"
      ]
    },
    {
      "state": "Kebbi",
      "senatorial_districts": [
        "Kebbi Central",
        "Kebbi North",
        "Kebbi South"
      ],
      "lgas": [
        "Aleiro",
        "Arewa-Dandi",
        "Argungu",
        "Augie",
        "Bagudo",
        "Birnin-Kebbi",
        "Bumza",
        "Dandi",
        "Danko",
        "Fakai",
        "Gwandu",
        "Jega",
        "Kalgo",
        "Koko-Besse",
        "Maiyama",
        "Ngaski",
        "Sakaba",
        "Shanga",
        "Suru",
        "Wasagu",
        "Yauri",
        "Zuru"
      ]
    },
    {
      "state": "Kaduna",
      "senatorial_districts": [
        "Kaduna Central",
        "Kaduna North",
        "Kaduna South"
      ],
      "lgas": [
        "Birnin-Gwari",
        "Chikun",
        "Giwa",
        "Gwagwada",
        "Igabi",
        "Ikara",
        "Jaba",
        "Jema'A",
        "Kachia",
        "Kaduna-North",
        "Kagarko",
        "Kajuru",
        "Kaura",
        "Kauru",
        "Koka\/Kawo",
        "Kubah",
        "Kudan",
        "Lere",
        "Makarfi",
        "Sabon-Gari",
        "Sanga",
        "Soba",
        "Tudun-Wada\/Makera",
        "Zango-Kataf",
        "Zaria"
      ]
    },
    {
      "state": "Kano",
      "senatorial_districts": [
        "Kano South",
        "Kano Central",
        "Kano North"
      ],
      "lgas": [
        "Ajingi",
        "Albasu",
        "Bagwai",
        "Bebeji",
        "Bichi",
        "Bunkure",
        "Dala",
        "Dambatta",
        "Dawakin-Kudu",
        "Dawakin-Tofa",
        "Doguwa",
        "Fagge",
        "Gabasawa",
        "Garko",
        "Garun-Mallam",
        "Gaya",
        "Gezawa",
        "Gwale",
        "Gwarzo",
        "Kano-Municipal",
        "Karaye",
        "Kibiya",
        "Kiru",
        "Kumbotso",
        "Kunchi",
        "Kura",
        "Madobi",
        "Makoda",
        "Minjibir",
        "Nasarawa",
        "Rano",
        "Rimin-Gado",
        "Rogo",
        "Shanono",
        "Sumaila",
        "Takai",
        "Tarauni",
        "Tofa",
        "Tsanyawa",
        "Tudun-Wada",
        "Ungogo",
        "Warawa",
        "Wudil"
      ]
    },
    {
      "state": "Kogi",
      "senatorial_districts": [
        "Kogi Central",
        "Kogi East",
        "Kogi West"
      ],
      "lgas": [
        "Adavi",
        "Ajaokuta",
        "Ankpa",
        "Dekina",
        "Ibaji",
        "Idah",
        "Igalamela",
        "Ijumu",
        "Ikoyi-Ijumu",
        "Kabba\/Bunu",
        "Kogi",
        "Lokoja",
        "Mopa-Muro-Mopi",
        "Obaji",
        "Ofu",
        "Ogori\/Magongo",
        "Okehi",
        "Okene",
        "Olamaboro",
        "Omala",
        "Oru",
        "Oyi",
        "Yagba-East",
        "Yagba-West"
      ]
    },
    {
      "state": "Katsina",
      "senatorial_districts": [
        "Katsina Central",
        "Katsina North",
        "Katsina South"
      ],
      "lgas": [
        "Bakori",
        "Batagarawa",
        "Batsari",
        "Baure",
        "Bindawa",
        "Charanchi",
        "Dan-Musa",
        "Dandume",
        "Danji",
        "Daura",
        "Dutsi",
        "Dutsinma",
        "Faskari",
        "Funtua",
        "Ingawa",
        "Jibia",
        "Kafur",
        "Kaita",
        "Kankara",
        "Kankia",
        "Katsina",
        "Kurfi",
        "Kusada",
        "Mai-Adua",
        "Malumfashi",
        "Mani",
        "Mashi",
        "Matazu",
        "Musawa",
        "Rimi",
        "Sabuwa",
        "Safana",
        "Sandamu",
        "Zango"
      ]
    },
    {
      "state": "Kwara",
      "senatorial_districts": [
        "Kwara Central",
        "Kwara North",
        "Kwara South"
      ],
      "lgas": [
        "Asa",
        "Baruten",
        "Edu",
        "Ekiti",
        "Ifelodun",
        "Ilorin south",
        "Ilorin west",
        "Ilorin east",
        "Irepodun",
        "Isin",
        "Kaiama",
        "Moro",
        "Offa",
        "Oke ero",
        "Oyun",
        "Pategi"
      ]
    },
    {
      "state": "Lagos",
      "senatorial_districts": [
        "Lagos West",
        "Lagos Central",
        "Lagos East"
      ],
      "lgas": [
        "Agege",
        "Ajeromi-Ifelodun",
        "Alimosho",
        "Amuwo-Odofin",
        "Apapa",
        "Badagry",
        "Epe",
        "Eti-Osa",
        "Ibeju-Lekki",
        "Ifako-Ijaiye",
        "Ikeja",
        "Ikorodu",
        "Kosofe",
        "Lagos-Island",
        "Lagos-Mainland",
        "Mushin",
        "Ojo",
        "Oshodi-Isolo",
        "Shomolu",
        "Somolu",
        "Surulere"
      ]
    },
    {
      "state": "Nassarawa",
      "senatorial_districts": [
        "Nassarawa South",
        "Nassarawa North",
        "Nassarawa West"
      ],
      "lgas": [
        "Akwanga",
        "Awe",
        "Doma",
        "Karu",
        "Keana",
        "Keffi",
        "Kokona",
        "Lafia",
        "Nassawara",
        "Nassawara Eggon",
        "Obi",
        "Wambu"
      ]
    },
    {
      "state": "Niger",
      "senatorial_districts": [
        "Niger East",
        "Niger North",
        "Niger South"
      ],
      "lgas": [
        "Agaie",
        "Agwara",
        "Bida",
        "Borgu",
        "Bosso",
        "Chanchaga",
        "Edati",
        "Gbako",
        "Gurara",
        "Katcha",
        "Kontagora",
        "Lapai",
        "Lavun",
        "Magama",
        "Mariga",
        "Mashegu",
        "Mokwa",
        "Muya",
        "Paikoro",
        "Rafi",
        "Rijau",
        "Shiroro",
        "Suleja",
        "Tafa",
        "Wushishi"
      ]
    },
    {
      "state": "Ogun",
      "senatorial_districts": [
        "Ogun Central",
        "Ogun East",
        "Ogun West"
      ],
      "lgas": [
        "Abeokuta-North",
        "Abeokuta-South",
        "Ado-Odo\/Ota",
        "Ewekoro",
        "Ifo",
        "Ijebu-East",
        "Ijebu-North",
        "Ijebu-North-East",
        "Ijebu-Ode",
        "Ikenne",
        "Imeko-Afon",
        "Ipokia",
        "Obafemi-Owode",
        "Odeda",
        "Odogbolu",
        "Ogun-Waterside",
        "Remo-North",
        "Sagamu",
        "Yewa North",
        "Yewa South"
      ]
    },
    {
      "state": "Ondo",
      "senatorial_districts": [
        "Ondo Central",
        "Ondo North",
        "Ondo South"
      ],
      "lgas": [
        "Akoko",
        "Akoko-North",
        "Akoko-North-West",
        "Akoko-South",
        "Akoko-South-East",
        "Akure",
        "Akure-North",
        "Akure-South",
        "Ese-Odo",
        "Idanre",
        "Ifedore",
        "Igbisin",
        "Ikale",
        "Ilaje",
        "Ilaje-West",
        "Ile-Oluji-Okeigbo",
        "Irele",
        "Odigbo",
        "Oka Ak0Ko",
        "Okiti Pupa Ijuodo",
        "Okiti-Pupa",
        "Ondo",
        "Ondo West",
        "Ondo-East",
        "Ose",
        "Owo"
      ]
    },
    {
      "state": "Osun",
      "senatorial_districts": [
        "Osun Central",
        "Osun East",
        "Osun West"
      ],
      "lgas": [
        "Atakumosa",
        "Atakumosa East",
        "Ayeda-Ade",
        "Ayedire",
        "Boluwaduro",
        "Boripe",
        "Ede",
        "Ede North",
        "Egbedore",
        "Ejigbo",
        "Ife",
        "Ife North",
        "Ife South",
        "Ife-Central",
        "Ife-East",
        "Ifelodun",
        "Ila",
        "Ilesa-East",
        "Ilesa-West",
        "Ilesha",
        "Ilesha West",
        "Irepodun",
        "Irewole",
        "Isokan",
        "Iwo",
        "Obokun",
        "Odo-Otin",
        "Ola Oluwa",
        "Olorunda",
        "Ori-Ade",
        "Orolu",
        "Osogbo"
      ]
    },
    {
      "state": "Oyo",
      "senatorial_districts": [
        "Oyo Central",
        "Oyo North",
        "Oyo South"
      ],
      "lgas": [
        "Afijio",
        "Akinyele",
        "Atiba",
        "Atisbo",
        "Egbeda",
        "Ibadan-Central",
        "Ibadan-North-East",
        "Ibadan-North-West",
        "Ibadan-South-East",
        "Ibadan-South-West",
        "Ibarapa-Central",
        "Ibarapa-East",
        "Ibarapa-North",
        "Ido",
        "Irepo",
        "Iseyin",
        "Itseiwaju",
        "Iwajowa",
        "Kajola",
        "Lagelu",
        "Odo-Oluwa",
        "Ogbomosho-North",
        "Ogbomosho-South",
        "Olorunsogo",
        "Oluyole",
        "Ona-Ara",
        "Orelope",
        "Ori-Ire",
        "Oyo-East",
        "Oyo-West",
        "Saki-East",
        "Saki-West",
        "Surulere"
      ]
    },
    {
      "state": "Plateau",
      "senatorial_districts": [
        "Plateau Central",
        "Plateau North",
        "Plateau South"
      ],
      "lgas": [
        "Barkin-Ladi",
        "Bassa",
        "Bokkos",
        "Jos-East",
        "Jos-North",
        "Jos-South",
        "Kanam",
        "Kanke",
        "Langtang-North",
        "Langtang-South",
        "Mangu",
        "Mikang",
        "Pankshin",
        "Quan'Anpan",
        "Riyom",
        "Shendam",
        "Wase"
      ]
    },
    {
      "state": "Rivers",
      "senatorial_districts": [
        "Rivers East",
        "Rivers South East",
        "Rivers West"
      ],
      "lgas": [
        "Aboa\/Odual",
        "Ahoada-East",
        "Ahoada-West",
        "Akukutoru",
        "Andoni",
        "Asari-Toru",
        "Bonny",
        "Buguma",
        "Degema",
        "Eleme",
        "Elfane",
        "Emuoha",
        "Etche",
        "Gokana",
        "Ikwerre",
        "Khana",
        "Obia\/Akpor",
        "Ogba-Egbema-Ndoni",
        "Ogba\/Egbema\/Ndoni",
        "Ogu\/Bolo",
        "Okirika",
        "Omuma",
        "Opobo\/Nkoro",
        "Oyigbo",
        "Port-Harcourt",
        "Tai"
      ]
    },
    {
      "state": "Sokoto",
      "senatorial_districts": [
        "Sokoto East",
        "Sokoto North",
        "Sokoto South"
      ],
      "lgas": [
        "Binji",
        "Bodinga",
        "Dange-Shuni",
        "Gada",
        "Goronyo",
        "Gudu",
        "Gwadabawa",
        "Illela",
        "Kebbe",
        "Kware",
        "Raba",
        "Sabo-Birni",
        "Shagari",
        "Silame",
        "Sokoto-North",
        "Sokoto-South",
        "Tambuwal",
        "Tangaza",
        "Tureta",
        "Wamakko",
        "Wurno",
        "Yabo"
      ]
    },
    {
      "state": "Taraba",
      "senatorial_districts": [
        "Taraba Central",
        "Taraba North",
        "Taraba South"
      ],
      "lgas": [
        "Ardo-Kola",
        "Bali",
        "Donga",
        "Gashaka",
        "Gassol",
        "Ibi",
        "Jalingo",
        "Karim-Lamido",
        "Kurmi",
        "Lau",
        "Oilingo",
        "Sardauna",
        "Takum",
        "Ussa",
        "Wukari",
        "Yorro",
        "Zing"
      ]
    },
    {
      "state": "Yobe",
      "senatorial_districts": [
        "Yobe East",
        "Yobe North",
        "Yobe South"
      ],
      "lgas": [
        "Bade",
        "Borsali",
        "Damaturu",
        "Fika",
        "Fune",
        "Geidam",
        "Gogaram",
        "Gujba",
        "Gulani",
        "Jakusko",
        "Karasuwa",
        "Machina",
        "Nangere",
        "Nguru",
        "Potiskum",
        "Tarmua",
        "Yunusari",
        "Yusufari"
      ]
    },
    {
      "state": "Zamfara",
      "senatorial_districts": [
        "Zamfara Central",
        "Zamfara North",
        "Zamfara West"
      ],
      "lgas": [
        "Anka",
        "Bakura",
        "Bukkuyum",
        "Bungudu",
        "Gumi",
        "Gusau",
        "Isa",
        "Kaura-Namoda",
        "Kiyawa",
        "Maradun",
        "Maru",
        "Shinkafi",
        "Talata-Mafara",
        "Tsafe",
        "Zurmi"
      ]
    }
  ];


// Code to fetch data

const stateSelect = document.getElementById("stateSelect");
const senatorialDistrictSelect = document.getElementById("senatorialDistrictSelect");
const lgaSelect = document.getElementById("lgaSelect");

// Populate the states dropdown
nigeriaStatesData.forEach(nigeriaStatesData => {
    const option = document.createElement("option");
    option.value = nigeriaStatesData.state;
    option.text = nigeriaStatesData.state;
    stateSelect.appendChild(option);
  });

// Function to populate senatorial districts and LGAs based on the selected state
function populateSenatorialDistrictsAndLGAs() {
    // Clear previous options
    senatorialDistrictSelect.innerHTML = "";
    lgaSelect.innerHTML = "";

    const selectedState = stateSelect.value;
    const selectedStateData = statesData.find(nigeriaStatesData => nigeriaStatesData.state === selectedState);

    if (selectedStateData) {
      // Populate senatorial districts
      selectedStateData.senatorial_districts.forEach(district => {
        const option = document.createElement("option");
        option.value = district;
        option.text = district;
        senatorialDistrictSelect.appendChild(option);
      });

      // Populate LGAs
      selectedStateData.lgas.forEach(lga => {
        const option = document.createElement("option");
        option.value = lga;
        option.text = lga;
        lgaSelect.appendChild(option);
      });
    }
  }