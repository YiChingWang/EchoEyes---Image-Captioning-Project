// JavaScript code to update the generated caption and display the uploaded image
document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  fetch("/generate_caption", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      //console.log(data); //打印响应数据以进行调试
      document.getElementById("caption").textContent = data.caption;

      // 更新音頻元素的src屬性並顯示播放器
      var audioPlayer = document.getElementById("caption-audio");
      audioPlayer.src = data.audio_path;
      audioPlayer.style.display = "block";
      audioPlayer.load();
      document.getElementById("image").src = URL.createObjectURL(
        formData.get("image")
      );
    });
});
