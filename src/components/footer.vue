<template>
    <div class="footer">
            <a class="footerlink" href="https://github.com/zayed-shamshad">
                <font-awesome-icon :icon="['fab', 'github']">
                </font-awesome-icon>
            </a>
            <a class="footerlink" href="https://instagram.com/zaid_shamshad">
                <font-awesome-icon :icon="['fab', 'instagram']"></font-awesome-icon>
            </a>
            <a class="footerlink" href="https://twitter.com/Zaidshamshad2">
                <font-awesome-icon :icon="['fab', 'twitter']"></font-awesome-icon>
            </a>
            <a class="footerlink" href="https://www.linkedin.com/in/mohammad-zaid-shamshad-611546203/">
                <font-awesome-icon :icon="['fab', 'linkedin']"></font-awesome-icon>
            </a>
        </div>
</template>

<script setup>
import { ref } from 'vue'
</script>
<style scoped>
.footer {
    height: 5vh;
    width: 100vw;
    
    background-color: rgb(0, 0, 0);
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Cairo', sans-serif;
    font-size: 1.2rem;
    color: #ffffff;
    padding: 0;
    box-shadow: 0px 0px 10px #000;
    left: 0;
    bottom: 0;
}
.footer svg {
    margin-left: 10px;
    margin-right: 10px;
}
</style>