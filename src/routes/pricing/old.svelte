<script>
    import PriceCard from '$lib/pricecard.svelte';
</script>

<div class=" flex flex-col items-center justify-center">
    <div class="min-w-full flex flex-col  justify-around ">


        <h1 class="py-5 text-3xl">Pricing</h1>
        <p>Thank you for considering me as your portrait photographer! Here is my pricing guide for portrait photography services based in Toronto:</p>

        <div class=" py-6 grid grid-rows-3 sm:divide-x divide-y-0 divide-y sm:grid-rows-none sm:grid-cols-3 ">
            <!-- Personal Portraits  -->
            <div class=" m-4 drop-shadow-xl drop card-body items-center text-center bg-orange-200">
                <h2 class="card-title text-2xl">Personal Portraits</h2>
                <p class="font-normal italic text-lg">Starting at $150</p>
                <span class="w-full my-2 pt-0.5 bg-neutral-900"></span>
                <div class="py-4 font-normal text-left h-full">
                    <p> ❖ One look</p>
                    <p> ❖ Choice of black or white backdrop</p>
                    <p> ❖ One professionally retouched image</p>
                    <p> ❖ Online gallery of 20-40 shots</p>
                </div>
            </div>
            <!-- Business Headshots  -->
            <div class=" m-4 drop-shadow-xl drop card-body items-center text-center bg-orange-200">
                <h2 class="card-title text-2xl">Business Headshots</h2>
                <p class="font-normal italic text-lg">Starting at $250</p>
                <span class="w-full my-2 pt-0.5 bg-neutral-900"></span>
                <div class="py-4 font-normal text-left h-full">
                    <p> ❖ One look</p>
                    <p> ❖ Choice of black or white backdrop</p>
                    <p> ❖ One professionally retouched image</p>
                    <p> ❖ Online gallery of 20-40 shots</p>
                </div>
            </div>
            <!-- Add-Ons  -->
            <div class=" m-4 drop-shadow-xl drop card-body items-center text-center bg-orange-200">
                <h2 class="card-title text-2xl">Add-ons</h2>
                <p class="font-normal italic text-lg">Extra</p>
                <span class="w-full my-2 pt-0.5 bg-neutral-900"></span>
                <div class="py-4 font-normal text-left h-full">
                    <p> ❖ $30 per additional retouched image</p>
                    <p> ❖ $100 per extra hour</p>
                    <p> ❖ $20 per extra look</p>
                </div>
            </div>

        </div>

        <div class="">
            <h1 class="my-6 text-3xl">Frequently Asked Questions</h1>
            <div class="my-4 collapse">
                <input type="checkbox" class="peer drop-shadow-md" />
                <div class="  rounded-full text-lg  collapse-title bg-orange-200 font-light ">
                    What To Expect During Your Photo Shoot?
                </div>
                <div class=" collapse-content">
                    <p class="font-normal mt-3">When you arrive for your session for headshots, we will spend a few minutes discussing some details. We will take a look at your clothing selections, and decide which will work best for your photo session and see what outfits will be best for the looks you are going for. It is a good idea to bring more than you need. It is better to have too much, than not enough options.</p>
                </div>
            </div>
            <div class="my-4 collapse">
                <input type="checkbox" class="peer" />
                <div class="rounded-full text-lg  collapse-title bg-orange-200 font-light ">
                    What To Expect During Your Photo Shoot?
                </div>
                <div class=" collapse-content">
                    <p class="font-normal mt-3">When you arrive for your session for headshots, we will spend a few minutes discussing some details. We will take a look at your clothing selections, and decide which will work best for your photo session and see what outfits will be best for the looks you are going for. It is a good idea to bring more than you need. It is better to have too much, than not enough options.</p>
                </div>
            </div>
            <div class="my-4 collapse">
                <input type="checkbox" class="peer" />
                <div class="rounded-full text-lg  collapse-title bg-orange-200 font-light ">
                    What To Expect During Your Photo Shoot?
                </div>
                <div class=" collapse-content">
                    <p class="font-normal mt-3">When you arrive for your session for headshots, we will spend a few minutes discussing some details. We will take a look at your clothing selections, and decide which will work best for your photo session and see what outfits will be best for the looks you are going for. It is a good idea to bring more than you need. It is better to have too much, than not enough options.</p>
                </div>
            </div>
            <div class="my-4 collapse">
                <input type="checkbox" class="peer" />
                <div class="rounded-full text-lg  collapse-title bg-orange-200 font-light ">
                    What To Expect During Your Photo Shoot?
                </div>
                <div class=" collapse-content">
                    <p class="font-normal mt-3">When you arrive for your session for headshots, we will spend a few minutes discussing some details. We will take a look at your clothing selections, and decide which will work best for your photo session and see what outfits will be best for the looks you are going for. It is a good idea to bring more than you need. It is better to have too much, than not enough options.</p>
                </div>
            </div>
            
        </div>
        

    </div>
</div>

<!-- OLD BACKGROUND COLOR - bg-slate-100 -->