
<template>
  <div class="flex flex-col min-h-screen m-0 p-0">
    <!-- Header -->
    <header class="text-black w-full">
      <div class="max-w-full mx-auto p-4">
        <span class="text-lg font-bold">
        <img src="@/assets/State Farm Logo.png" alt="State Farm Logo" class="h-32"> <!-- Adjust the path to your logo and the height class as needed -->
        </span>
        <span class="text-3xl font-bold">Introducing JakeBot.</span>
      </div>
    </header>

    <!-- Body -->
    <main class="flex-grow container mx-auto flex flex-col items-center justify-center p-4 text-center">
      <h1 class="text-2xl font-bold mb-2">This is not an ordinary chat bot. Jake is powered by Google's Dialogflow and Vertex AI,
        utilizing large language models for human-like interactions, offering quick insurance services to small businesses.</h1>
      <p class="text-lg mb-2">Jake harnesses advanced AI to deliver fast and comprehensive
        insurance solutions, eliminating the need for link redirections or phone calls to representatives.</p>
      <p>This is more than an AI chatbot. With an easily adaptable and expandable suite of AI tools offered by Google Cloud,
      this is a revolution in insurance. Try it today ></p>
      <span class="text-lg font-bold mt-5">
        <img src="@/assets/TechStack.png" alt="Tech Stack img" class="h-60"> <!-- Adjust the path to your logo and the height class as needed -->
        </span>
      <p class="text-gray-400">Made with &lt3 (and caffiene) at HackUTD 2023</p>
    </main>

    <!-- Footer -->
    <footer class="text-black w-full">
      <div class="max-w-full mx-auto p-4 flex justify-between">
        <a href="https://github.com/nafizzl/HackUTD2023" class="hover:text-gray-600">GitHub</a>
        <a href="https://devpost.com/software/jakebot" class="hover:text-gray-600">Devpost</a>
        <p>Faris Shaik / Nafiz Labib / Murtaza Khan / Zohaib Saqib</p>

      </div>
    </footer>
  </div>
</template>

<!-- No need for the <style> section as Tailwind CSS is being used -->

<script>
export default {
  method: {

  },
  mounted() {
    (function(d, m){
        var kommunicateSettings = 
            {"appId":"10477a11ac9aab5f5db89d9c5bdbac6e3","popupWidget":true,"automaticChatOpenOnNavigation":true};
        var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
        s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
        var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
        window.kommunicate = m; m._globals = kommunicateSettings;
    })(document, window.kommunicate || {});
    /* NOTE : Use web server to view HTML files as real-time update will not work if you directly open the HTML file in the browser. */
    
  }
}
</script>


