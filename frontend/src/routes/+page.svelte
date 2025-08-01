<script lang="ts">
    import {Splide, SplideSlide, SplideTrack} from '@splidejs/svelte-splide';
    import {Button} from 'bits-ui';
    import '@splidejs/svelte-splide/css';
    import '@splidejs/svelte-splide/css/core';
    import image1 from '$lib/assets/wallhaven-m9kdw9.png';
    import image2 from '$lib/assets/wallhaven-zyr66w.jpg'
    import {generateSlides} from '../utils'


    const slides = generateSlides();
    const options = {
        rewind: true, 
        arrows:false, 
        autoplay:true,

    }
</script>

<div>
    <Splide options={ options } aria-label="My Favorite Images">
        <SplideSlide>
            <div class="relative w-full h-[600px]">
                <!-- Background Image -->
                <enhanced:img
                class="w-full h-full object-cover mask-b-from-20% mask-b-to-80%"
                src="$lib/assets/wallhaven-m9kdw9.png"
                alt="Chainsawman"
                />

                <!-- Overlay Info -->
                <div
                class="absolute inset-0 flex items-center justify-start px-8"
                >
                    <div class="text-white max-w-md lg:mx-10">
                        <!-- Category -->
                        <span class="text-sm font-semibold text-yellow-400">
                        Action • Horror
                        </span>

                        <!-- Title -->
                        <h2 class="text-3xl font-bold mt-2">Chainsawman</h2>

                        <!-- Description -->
                        <p class="mt-3 text-base leading-relaxed opacity-90">
                        Denji is a young man trapped in poverty, working off his deceased
                        father’s debt by working as a Devil Hunter with his pet devil Pochita.
                        </p>

                        <!-- Buttons -->
                        <div class="mt-4 flex gap-3">
                            <Button.Root
                                class="rounded-input bg-white text-gray-900 shadow-lg 
                                    hover:bg-white px-6 py-2 text-sm font-semibold
                                    active:scale-[0.98] active:transition-all"
                            >
                                Read Now
                            </Button.Root>

                            <Button.Root
                                class="rounded-input bg-gray-800 text-white shadow-lg 
                                    hover:bg-gray-700 px-6 py-2 text-sm font-semibold
                                    active:scale-[0.98] active:transition-all"
                            >
                                Favorit
                            </Button.Root>
                        </div>
                    </div>
                </div>
            </div>
        </SplideSlide>

        <SplideSlide>
            <div class="relative w-full h-[600px]">
                <!-- Background Image -->
                <enhanced:img
                class="w-full h-full object-cover mask-b-from-20% mask-b-to-80%"
                src="$lib/assets/wallhaven-zyr66w.jpg"
                alt="soloLeveling"
                />

                <!-- Overlay Info -->
                <div
                class="absolute inset-0 flex items-center justify-start px-8"
                >
                    <div class="text-white max-w-md lg:mx-10">
                        <!-- Category -->
                        <span class="text-sm font-semibold text-yellow-400">
                        Action • Adeventur
                        </span>

                        <!-- Title -->
                        <h2 class="text-3xl font-bold mt-2">Solo leveling</h2>

                        <!-- Description -->
                        <p class="mt-3 text-base leading-relaxed opacity-90">
                        Denji is a young man trapped in poverty, working off his deceased
                        father’s debt by working as a Devil Hunter with his pet devil Pochita.
                        </p>

                        <!-- Buttons -->
                        <div class="mt-4 flex gap-3">
                            <Button.Root
                                class="rounded-input bg-white text-gray-900 shadow-lg 
                                    hover:bg-white px-6 py-2 text-sm font-semibold
                                    active:scale-[0.98] active:transition-all"
                            >
                                Read Now
                            </Button.Root>

                            <Button.Root
                                class="rounded-input bg-gray-800 text-white shadow-lg 
                                    hover:bg-gray-700 px-6 py-2 text-sm font-semibold
                                    active:scale-[0.98] active:transition-all"
                            >
                                Favorit
                            </Button.Root>
                        </div>
                    </div>
                </div>
            </div>
        </SplideSlide>
        <div class="splide__progress">
            <div class="splide__progress__bar">
            </div>
        </div>
    </Splide>
</div>

<style lang="postcss">
    @reference "tailwindcss";
</style>