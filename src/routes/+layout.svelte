<script defer>
    import "../app.css";

    let checkbox;
 
    function check(){
        checkbox.checked = !checkbox.checked;
    }

</script>

<div class="mx-6 sm:mx-10 flex antialiased font-semibold font-body">
    <div class="drawer drawer-mobile">
        <input bind:this={checkbox} id="my-drawer-2" type="checkbox" class="drawer-toggle" />
        <div class="drawer-content flex flex-col items-center py-10 scrollbar-hide">
            <!-- Page content here -->
            <div class=" w-full z-10 absolute h-auto top-0 grid grid-cols-4 bg-white lg:hidden">
                <label for="my-drawer-2" class="justify-self-start self-center "><img class="m-6 md:m-10 w-8" src="/sidebar.png"></label>
                <a class="col-span-2 flex flex-col justify-center items-center " href="/">
                    <img class="md:w-3/5 w-4/5 h-auto" src="https://www.kadencewp.com/wp-content/uploads/2020/10/alogo-4.png">
                </a>
                <!-- <div></div> -->
               
            </div>
            <div class="lg:my-0 md:mt-40 mt-16 flex flex-col w-full">
                <slot />
            </div>

        
        </div> 
        <!-- get rid of border from below once done testing -->
        <div class="text-lg drawer-side ">
            <label for="my-drawer-2" class="hidden drawer-overlay"></label> 
            <ul class="items-center menu p-4 w-5/6 bg-base-100 text-base-content">
                <!-- Sidebar content here -->
                <label for="my-drawer-2" class="self-end lg:hidden"><img class="w-6" src="/close.png"></label>
                <div class="pr-10">
                    <a on:click={event => check()} href='/'><p class="w-full text-center"></p><img class="w-80" src="https://www.kadencewp.com/wp-content/uploads/2020/10/alogo-4.png"></a>
                    <!-- <li on:click={event => check()} class=" w-full"><a href='/'><p class="w-full text-center"></p>Home</p></a></li> -->
                    <li on:click={event => check()} class="w-full"><a href='/about'><p class="w-full text-center">About</p></a></li>
                    <div class=" dropdown  p-3 w-full grid grid-cols-1 place-content-center hover:bg-neutral-200">
                        <label tabindex="0" class="cursor-pointer text-center w-full">Portfolio</label>
                        <ul tabindex="0" class="w-full dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
                            <li on:click={event => check()} class="w-full "><a href='/portraits'><p class="z-50 w-full text-center">Portraits</p></a></li>
                            <li on:click={event => check()} class="w-full"><a href='/street'><p class="w-full text-center">Street</p></a></li>
                            <li on:click={event => check()} class="w-full"><a href='/travel'><p class="w-full text-center">Travel</p></a></li>
                            <li on:click={event => check()} class="w-full"><a href='/events'><p class="w-full text-center">Events</p></a></li>
                        </ul>
                    </div>
                    <li on:click={event => check()} class="w-full"><a href='https://stanik.darkroom.com/'><p class="w-full text-center">Prints</p></a></li>
                    <li on:click={event => check()} class="w-full"><a href='/pricing'><p class="w-full text-center">Pricing</p></a></li>
                    <li on:click={event => check()} class="w-full"><a href='/contact'><p class="w-full text-center">Contact</p></a></li>
                </div>
                

            </ul>
        </div>
    </div>
</div>
  
