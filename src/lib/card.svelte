<script>
    export let side = "left"
    export let text = "Null"
    export let img
    export let internalLink


    function link(Link){
        window.location.href = Link;
    }
</script>

<!-- <div on:click={event => window.location.href = internalLink} class="hover:scale-105 transition-all ease-in delay-100 my-5 sm:w-3/4 h-2/5 flex sm:flex-row aspect-square sm:aspect-auto flex-col bg-slate-200 hover:grayscale hover:cursor-pointer"> -->
    {#if side === "left"}
        <div on:click={event => window.location.href = internalLink} class="drop-shadow-lg border border-black hover:scale-105 transition-all ease-in delay-100 my-5 sm:w-3/4 h-72 flex sm:flex-row aspect-square sm:aspect-auto flex-col bg-stone-50 text-neutral-800 hover:grayscale hover:cursor-pointer">
            <img class="object-cover relative h-full w-full" src={img}>
            <div class="flex items-center justify-center aspect-square p-6 sm:w-2/5 sm:h-full h-1/5">
                <h1 class="self-center text-2xl text-center">{text}</h1>
            </div>
        </div>

    {:else if side === "right"}
        <div on:click={event => window.location.href = internalLink} class="drop-shadow-lg border border-black hover:scale-105 transition-all ease-in delay-100 my-5 sm:w-3/4 h-72 flex sm:flex-row-reverse aspect-square sm:aspect-auto flex-col bg-stone-50 text-neutral-800 hover:grayscale hover:cursor-pointer">
            <img class="object-cover relative h-full w-full" src={img}>
            <div class="flex items-center justify-center aspect-square p-6 sm:w-2/5 sm:h-full h-1/5">
                <h1 class="self-center text-2xl text-center">{text}</h1>
            </div>
        </div>

    {/if}
    
<!-- </div> -->