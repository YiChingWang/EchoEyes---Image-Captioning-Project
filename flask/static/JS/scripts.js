document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  fetch("/generate_caption", {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok " + response.statusText);
      }
      return response.json();
    })
    .then((data) => {
      document.getElementById("caption").textContent = data.caption;

      var audioPlayer = document.getElementById("caption-audio");
      audioPlayer.src = data.audio_path;
      audioPlayer.style.display = "block";
      audioPlayer.load();

      document.getElementById("image").src = URL.createObjectURL(
        formData.get("image")
      );
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
      document.getElementById("caption").textContent =
        "An error occurred while processing your request. Please try again.";
      document.getElementById("caption-audio").style.display = "none";
      document.getElementById("image").src = ""; 
    });
});
