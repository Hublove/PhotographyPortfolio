<script>
    import PriceCard from '$lib/pricecard.svelte';
</script>
<div class="flex flex-col w-full items-center py-6">

    <div class="lg:w-11/12 flex flex-col items-center justify-center">
        <div class="min-w-full flex flex-col  justify-around ">


            <h1 class="mb-6 text-5xl font-bold">Pricing</h1>
            <p class="font-normal">Thank you for considering me as your portrait photographer! If you have any questions or special requests dont hesitate to get in contact with me so that we can better met your needs. Here is my pricing guide for portrait photography services based in Toronto:</p>

            <div class="flex lg:flex-row flex-col justify-around mt-8">
                <div class="border border-black lg:w-1/3 py-6 px-8 m-6 drop-shadow-xl items-center text-center bg-stone-50">
                    <h2 class="text-2xl">Personal Portraits</h2>
                    <p class="font-normal italic text-lg">Starting at $250</p>
                    <hr class="mt-4 mb-2 h-0.5 border-t-0 bg-black opacity-70" />
                    <div class="py-4 font-normal text-left">
                        <p> ❖ 1 hour session </p>
                        <p> ❖ One professionally retouched image</p>
                        <p> ❖ Online gallery of 20-40 shots</p>
                    </div>
                </div>
                <div class="border border-black lg:w-1/3 py-6 px-8 m-6 drop-shadow-xl items-center text-center bg-stone-50">
                    <h2 class="text-2xl">Business Headshots</h2>
                    <p class="font-normal italic text-lg">Starting at $350</p>
                    <hr class="mt-4 mb-2 h-0.5 border-t-0 bg-black opacity-70" />
                    <div class="py-4 font-normal text-left">
                        <p> ❖ 0.5 hour session </p>
                        <p> ❖ Choice of backdrop </p>
                        <p> ❖ One professionally retouched image</p>
                        <p> ❖ Online gallery of 20-40 shots</p>
                    </div>
                </div>
                <div class="border border-black lg:w-1/3 py-6 px-8 m-6 drop-shadow-xl items-center text-center bg-stone-50">
                    <h2 class="text-2xl">Add-ons</h2>
                    <p class="font-normal italic text-lg">Extra</p>
                    <hr class="mt-4 mb-2 h-0.5 border-t-0 bg-black opacity-70" />
                    <div class="py-4 font-normal text-left">
                        <p> ❖ $20 per extra look</p>
                        <p> ❖ $30 per additional retouched image</p>
                        <p> ❖ $100 per extra hour</p>
                    </div>
                </div>
            </div>

            <div class="">
                <h1 class="my-6 text-3xl font-bold">Frequently Asked Questions</h1>
                <div class=" my-4  collapse">
                    <input type="checkbox" class="peer border" />
                    <div class="drop-shadow-xl text-lg border-2 border-b-0 border-black bg-black text-white collapse-title ">
                        What To Expect During Your Photo Shoot?
                    </div>
                    <div class="drop-shadow-xl border-black border collapse-content bg-stone-50">
                        <p class="font-normal mt-3">During your photo shoot, you can expect a professional and friendly atmosphere where your vision and preferences are valued. I will guide you through various poses and compositions to capture your unique personality and create stunning images. After the session, you will receive a Google Drive link which contains your images. From there you can review and choose which images you'd like retouched. You can expect timely delivery of the final edited photos, typically within two weeks.</p>
                    </div>
                </div>
                <div class=" my-4  collapse">
                    <input type="checkbox" class="peer border" />
                    <div class="drop-shadow-xl text-lg border-2 border-b-0 border-black bg-black text-white collapse-title ">
                        How Do I See My Photographs?
                    </div>
                    <div class="drop-shadow-xl border-gray-900 border collapse-content bg-stone-50">
                        <p class="font-normal mt-3">Within 24hrs of your shoot you will be emailed a Google Drive link with a gallery of your shoot. You can make your selection here on which of your images you'd like retouched. Within 2 weeks of your shoot you will be emailed a separate Google Drive link with your retouched photos.</p>
                    </div>
                </div>
                <div class=" my-4  collapse">
                    <input type="checkbox" class="peer border" />
                    <div class="drop-shadow-xl text-lg border-2 border-b-0 border-black bg-black text-white collapse-title ">
                        What Is Retouching?
                    </div>
                    <div class="drop-shadow-xl border-gray-900 border collapse-content bg-stone-50">
                        <p class="font-normal mt-3"> It involves making adjustments to various elements like color, contrast, sharpness, and removing imperfections. Retouching can be used to enhance the overall appearance of a photo, correct minor flaws, or achieve a specific artistic vision. The goal is to refine and improve the overall aesthetic quality of the photograph while maintaining its authenticity. Professional retouching can greatly enhance the visual impact of your images and bring out the best in your subjects.</p>
                    </div>
                </div>
                

                
            </div>
            

        </div>
    </div>
</div>




<!-- OLD BACKGROUND COLOR - bg-gray-900 -->

