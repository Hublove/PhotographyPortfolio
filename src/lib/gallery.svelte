<script>

    export let category


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
        console.log(category)
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
        
        fetch("/" + category +".json")
            .then((res) => {
                if (!res.ok) throw new Error('Fetch error');
                return res;
            })
            .then((res) => res.json());
  
</script> 



<div id="images" class="flex flex-wrap justify-center gap-10 mx-3">
    {#if imagesPromise}
        {#await imagesPromise}
            <h1>Loading...</h1>
        {:then images}
            {#each imageLinks as image, index}
                <a bind:this={image.element} class="hover:scale-105 transition-all ease-in delay-100 self-center align-center " on:click={event => openGallery(event)}
                    href={image.img}
                    data-thumb={image.thumb}
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
