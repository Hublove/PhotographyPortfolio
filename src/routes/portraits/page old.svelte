<!-- <script>
    import Gallery from 'svelte-gallery';
  
    const images = [
      { src: 'https://source.unsplash.com/random', width: 600, height: 400 },
      { src: 'https://source.unsplash.com/random', width: 400, height: 600 },
      { src: 'https://source.unsplash.com/random', width: 800, height: 1200 },
      { src: 'https://source.unsplash.com/random', width: 300, height: 200 }
    ];
  </script>
  
<Gallery {images} /> -->

<!-- <script>
	import PhotoswipeGallery from 'svelte-photoswipe-gallery';

    function loadImages() {
        const fs = require("fs");
        fs.readdirSync(".levels/").forEach(file => {
            //Print file name
            console.log(file)

            /*
            Run this to print the file contents
            console.log(readFileSync(".levels/" + file, {encoding: "utf8"}))
            */
        })
    }
    

        

	const images = [
		{
			src: 'https://source.unsplash.com/random',
			preview: 'https://source.unsplash.com/random',
			width: 400,
			height: 600,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
		{
			src: 'https://source.unsplash.com/random',
			width: 800,
			height: 1200,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
		{
			src: 'https://source.unsplash.com/random',
			width: 300,
			height: 200,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
        {
			src: 'https://source.unsplash.com/random',
			width: 300,
			height: 200,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
        {
			src: 'https://source.unsplash.com/random',
			width: 300,
			height: 200,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
        {
			src: 'https://source.unsplash.com/random',
			width: 300,
			height: 200,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
        {
			src: 'https://source.unsplash.com/random',
			width: 300,
			height: 200,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
        {
			src: 'https://source.unsplash.com/random',
			width: 300,
			height: 200,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		},
		{
			src: 'https://source.unsplash.com/random',
			width: 600,
			height: 400,
			description: 'Lorem ipsum dolor sit amet',
			alt: 'Random'
		}
	];
</script> 

<PhotoswipeGallery 
	{images}
	showDescription="{false}"
	showDownloadButton="{false}"
	showFullscreenButton="{true}"
/> -->

<script>
    import BiggerPicture from 'bigger-picture/svelte'

    // import style
    import "bigger-picture/css";
    // import "./style.css";

    // initialize BiggerPicture
    import { onMount } from 'svelte';
	import { self } from 'svelte/internal';
    let bp = null
    let imageLinks = []
    $: imagesPromise = null
    onMount(() => {
        bp = BiggerPicture({
            target: document.body
        });
        // grab image links
        imagesPromise = loadGallery();
        // imageLinks = document.querySelectorAll("#images > a");
        const getGallery = async () => {
            imageLinks = await imagesPromise;
            console.log(imageLinks);
        };

        getGallery()
        
    });



    
    // open BiggerPicture
    function openGallery(e) {
        e.preventDefault();
        console.log(e.currentTarget)
        bp.open({
            items: imageLinks,
            el: e.currentTarget,
            intro: "fadeup"
        });
    }

    
    const loadGallery = () =>
        fetch(`/sample.json`)
            .then((res) => {
                if (!res.ok) throw new Error('Fetch error');
                return res;
            })
            .then((res) => res.json());
  
</script> 



<div id="images" class="flex flex-wrap justify-center gap-10 ">
    {#if imagesPromise}
        {#await imagesPromise}
            <h1>Loading...</h1>
        {:then images}
            {#each imageLinks as image, index}
                <a bind:this={image.element} class="hover:scale-105 transition-all ease-in delay-100 self-center align-center " on:click={event => openGallery(event)}
                    href={image.img}
                    data-thumb={image.img}
                    data-height={image.height}
                    data-width={image.width}
                    data-alt={image.alt}
                >
                    <img
                    class="object-cover w-96 h-96 align-middle "
                    src={image.thumb}
                    alt={image.alt}
                    />
                </a>
            {/each}
        {:catch err}
            <pre>{err}</pre>
        {/await}
    {/if}
</div>
