
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

document.getElementById('filter-icon').addEventListener('onclick', function(){
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

document.getElementById('filter-icon').addEventListener('onclick', function(){
    displayFilteredSearchBox2();
    hideFilteredPropBox2();
});



// To Diplay Filter Search Box - 
// To allow user interract with options to filter search  
function displayPropertyDetailsOverlay(propertyID) {
    var property_details_overlay_box = document.getElementById('property-details-overlay-'+propertyID);

    if (property_details_overlay_box.style.display === 'none' || property_details_overlay_box.style.display === '') {
        property_details_overlay_box.style.display = 'block';
    } else {
        property_details_overlay_box.style.display = 'none';
    }

}
var property_display_box = document.getElementById('property-display-box');
property_display_box.addEventListener('onmouseover', displayPropertyDetailsOverlay);


// function hidePropertyDetailsOverlay() {
//     // const filter_icon = document.getElementById('filter-icon');
//     var property_details_overlay_box = document.getElementById('property-details-overlay');

//     if (property_details_overlay_box.style.display === 'block') {
//         property_details_overlay_box.style.display = 'none';
//     } else {
//         property_details_overlay_box.style.display = 'none';
//     }

// }
// var property_display_box = document.getElementById('property-details-overlay');
// property_display_box.addEventListener('onmouseover', hidePropertyDetailsOverlay);



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


// To Diplay Upload Property buttton Icon Label - 
// Enables user to know what the button icon is for 
// function displayUploadPropertyLabel() {
//     var upload_property_name = document.getElementById('upload-property-label');

//     if (upload_property_name.style.display === 'none' || upload_property_name.style.display === '') {
//         upload_property_name.style.display = 'flex';
//     } else {
//         upload_property_name.style.display = 'none';
//     }

// }
// var upload_property_icon = document.getElementById('upload-property-label');
// upload_property_icon.addEventListener('onmouseover', displayUploadPropertyLabel);


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
filter_icon.addEventListener('onclick', changeBookMarkIcon);



// To display commercial property sub-choices - 
// Enables user to choose sub-choice for commercial property 
function showCommercialPropSub(){
    const commercial_sub_prop = document.getElementById('Commercial-property-sub');  
    if (commercial_sub_prop.style.display === 'none' || commercial_sub_prop.style.display === ''){
        commercial_sub_prop.style.display = 'block';
    } else {
        commercial_sub_prop.style.display = 'none';
    }
}
var commercial_prop = document.getElementById('Commercial-property');
commercial_prop.addEventListener('onclick', showCommercialPropSub)


function showCommercialPropSub2(){
    const commercial_sub_prop = document.getElementById('Commercial-property-sub');  
    if (commercial_sub_prop.style.display === 'block' || commercial_sub_prop.style.display === ''){
        commercial_sub_prop.style.display = 'none';
    } else {
        commercial_sub_prop.style.display = 'none';
    }
}
var com_sub_prop1 = document.getElementById('Com-option-1');
com_sub_prop1.addEventListener('onclick', showCommercialPropSub2)

var com_sub_prop2 = document.getElementById('Com-option-2');
com_sub_prop2.addEventListener('onclick', showCommercialPropSub2)

var com_sub_prop3 = document.getElementById('Com-option-3');
com_sub_prop3.addEventListener('onclick', showCommercialPropSub2)

var com_sub_prop4 = document.getElementById('Com-option-4');
com_sub_prop4.addEventListener('onclick', showCommercialPropSub2)

var com_sub_prop5 = document.getElementById('Com-option-5');
com_sub_prop5.addEventListener('onclick', showCommercialPropSub2)

var com_sub_prop6 = document.getElementById('Com-option-6');
com_sub_prop6.addEventListener('onclick', showCommercialPropSub2)

var com_sub_prop7 = document.getElementById('Com-option-7');
com_sub_prop7.addEventListener('onclick', showCommercialPropSub2)

var com_sub_prop8 = document.getElementById('Com-option-8');
com_sub_prop8.addEventListener('onclick', showCommercialPropSub2)


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



       