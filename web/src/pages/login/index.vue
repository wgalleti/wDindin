<template>
  <div class="w-full h-full flex justify-between">
    <div class="flex justify-center items-center w-full">
      <h1 class="text-4xl text-green-700 animate-pulse duration-300 ease-in-out">WDindin</h1>
    </div>
    <div class="w-[600px] h-auto p-6 rounded-md bg-white/5">
      <Login />
    </div>
  </div>
</template>

<script setup>
import Login from '@/components/auth/Login.vue'
</script>
