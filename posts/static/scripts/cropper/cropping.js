
const imageBox = document.getElementById('imageBox')
const imageForm = document.getElementById('imageForm')
const confirmBtn = document.getElementById('confirmBtn')
const input = document.getElementById('id_profile_pic')
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;


input.addEventListener('change', ()=>{
  confirmBtn.classList.remove('visible')
  const img_data = input.files[0]
  const url = URL.createObjectURL(img_data)
  imageBox.innerHTML = `<img src="${url}" id="image" width="300px" height="300px"/>`
  const image = document.getElementById('image');

  const cropper = new Cropper(image, {
    aspectRatio: 1 / 1,
    crop: function(event) {
  }
  });
  confirmBtn.addEventListener('click', (event) => {
    event.preventDefault();
    var modal = new bootstrap.Modal(document.getElementById('modal'));
    // Get the cropped image as a Blob
    cropper.getCroppedCanvas().toBlob((blob) => {
      // Create a FormData object and append the blob data
      const formData = new FormData();
      formData.append('profile_pic', blob, img_data.name); // Adjust the file name as needed

      // Make an AJAX request
      $.ajax({
        type: 'POST',
        url: '/en/members/changeProfileImage',
        headers: {
          'X-CSRFToken': csrfToken, // Include the CSRF token in the headers
        },
        processData: false,
        contentType: false,
        data: formData,
        success: (response) => {
          console.log(response);
          if (response.close==true) {
            location.reload(true);
          }
      },
        error:  function(xhr, textStatus, errorThrown) {
          modal.hide();
          console.log(modal)
        },
      });
    });
  });
});