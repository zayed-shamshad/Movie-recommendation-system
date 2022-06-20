<template>
    <div class="search-outerbox">
        <div class="search-innerbox">
            <!-- <div class="search-title">
                Type in the name of the movie
            </div> -->
            <input type="text" v-model="movie" placeholder="Enter the movie name...">
            <button @click="makeRequest" class="search-movie">
                Search
            </button>
        </div>
    </div>

    <div class="movie-outerbox">
        <div class="image-bg1">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis

            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,



        </div>
        <div class="image-bg2">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis

            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,



        </div>
        <div class="image-bg3">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis

            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            s sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,
            nam sed fuga incidunt dicta amet eos pariatur corporis iste voluptas cum et! Iste. Lorem ipsum dolor, sit
            amet consectetur adipisicing elit. Alias unde maiores eos vitae nemo, iusto sapiente exercitationem dolore
            ipsum cum vero expedita cumque neque aut repellendus cupiditate nesciunt culpa facere.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam impedit rem eos sunt, laborum ipsum iste
            vitae saepe error esse earum sed suscipit neque amet, tenetur hic. Ex, in maxime. Lorem ipsum dolor sit
            amet, consectetur adipisicing elit. Dolorem quidem rerum perspiciatis. Iste pariatur qui cumque, facilis
            ducimus iusto, eius culpa, possimus quasi a impedit? Incidunt, quidem. Molestias, dolor error!
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto ad, dolore nostrum qui harum ea officia,



        </div>
        <div class="wave" v-if="load">
            <div v-for="i in 30" :key='i' class="wave-inner" :id="i">
            </div>
        </div>
        <div class="movie-box" v-else>
            <font-awesome-icon icon="close" @click="closebox"></font-awesome-icon>
            <poster :title="movies[ind]" :link="links[ind]" :review="overview[ind]">
            </poster>
            <div class="bottom-buttons">
                <div>
                    Get more info
                </div>
                <button @click="changemovie">
                    Next
                </button>
                <div @click="addtofav" class="heart">❤</div>
            </div>
        </div>

    </div>
</template>
<script>
import axios from 'axios'
import poster from './poster.vue'
import {db} from '../firebase.js'
import { doc, setDoc, getDoc } from "firebase/firestore";
import { getAuth } from "firebase/auth";
import { onAuthStateChanged} from 'firebase/auth';
export default {
    name: 'search',
    components: {
        poster
    },
    data(){
        return{
            load:true,
            movies:[],
            overview:[],
            movie:'eg: batman...',
            links:[],
            ind:0,
            fav:{}
        }
    },
    mounted(){
        this.wave();
        console.log(this.fav);
        onAuthStateChanged(getAuth(), async (user) => {
            if (user) {
                const docRef = doc(db, "users", user.email);
                const docSnap = await getDoc(docRef);
                if (docSnap.exists()) {
                    this.fav=docSnap.data();
                }
                else{
                    console.log("mo fav");
                }
                console.log(this.fav);
            } else {
                console.log("No user is signed in");
            }
       });

    },
    methods:{
        closebox(){
            this.load=true;
        },
        wave(){
          const k = document.getElementsByClassName('wave-inner');
          for (let i = 0; i < k.length; i++) {
              k[i].style.animation = 'wave 1s ease-in-out infinite';
              k[i].style.animationDelay = i * 0.05 + 's';
              k[i].style.backgroundColor = "red";
          }
            },
        async addtofav(){
            var user = getAuth().currentUser;
            if (this.movies[this.ind] in this.fav){
                document.getElementsByClassName('heart')[0].style.color = "pink";
                delete this.fav[this.movies[this.ind]];
            }
            else{
            this.fav[this.movies[this.ind]] = this.movies[this.ind];
            document.getElementsByClassName('heart')[0].style.color = "red";
            }
            await setDoc(doc(db, "users",  user.email),this.fav);

        },
        changemovie(){
            if(this.ind<this.movies.length-1){
                this.ind++;
            }
            else{
                this.ind=0; }
            if (this.movies[this.ind] in this.fav) {
                document.getElementsByClassName('heart')[0].style.color = "red";
            }
            else{
                document.getElementsByClassName('heart')[0].style.color = "pink";
            }
        },
        makeRequest(){
            const path = "https://movie-api-backend-a-z.herokuapp.com/"
            document.getElementsByClassName('wave')[0].style.display="flex";
            this.wave();
            axios.get(path + this.movie)
                .then(response => {
                    this.movies = Object.keys(response.data['1'])
                    this.overview = Object.values(response.data['2'])
                    this.links= Object.values(response.data['1'])
                }) 
                .catch(error => {
                    console.log(error)
                }) 
                .finally(() => (
                    document.getElementsByClassName('wave')[0].style.display = "none",
                    this.load=false
                ));
                // setTimeout(() => {
                //     if (this.movies[this.ind] in this.fav) {
                //         document.getElementsByClassName('heart')[0].style.color = "yellow";
                //         delete this.fav[this.movies[this.ind]];
                //     }
                //     else {
                //         this.fav[this.movies[this.ind]] = this.movies[this.ind];
                //         document.getElementsByClassName('heart')[0].style.color = "blue";
                //     }
                // }, 3000);
        }
    }
}
</script>
<style>





.image-bg1{
    background:url('src/assets/harley.jpg');
    background-size: cover;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    width:400px;
    line-height: 2px;
height: 60vh;
    top:5vh;
    position:absolute;
    font-size: 10px;
    font-weight: bold;
    left:0;
}
.image-bg2 {
    background: url('src/assets/2001.jpg');
    background-size: cover;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    width: 400px;
    line-height: 2px;
    height: 60vh;
    top: 5vh;
    position: absolute;
    font-size: 10px;
    font-weight: bold;
    left: 50vw;
    transform: translateX(-50%);
}
.image-bg3{
    background: url('src/assets/blackwidow.jpg');
    background-size: cover;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    width: 400px;
    line-height: 2px;
    height: 60vh;
    top: 5vh;
    position: absolute;
    font-size: 10px;
    font-weight: bold;
    right: 0;
}
.movie-outerbox{
    display:flex;
    position:absolute;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    height:80vh;
    width:100vw;
    top:20vh;
    background-color:rgb(238, 233, 233);
    z-index:-10;
}

.search-title{
    font-size: 3em;
    font-weight: bold;
    text-align: center;
    font-family: 'Limelight', cursive;
}
.heart{
    font-size: 2.5em;
    cursor:pointer;
    transition: all 0.24s ease-in-out;
    margin-top: 70px;
}
.heart:hover{
    transform:scale(1.2);

}

.filled-in {
    font-weight: 900;
}

.bottom-buttons{
    display:flex;
    justify-content: space-evenly;
    flex-direction: column;
    margin:10px;
}
.bottom-buttons button{
    height:30px;
    width:80px;
    border-radius:5px;
    border:none;
    background-color: rgb(31, 20, 17);
    color:white;
    font-size: 1rem;
    font-weight: bold;
    transition:all 0.2s ease-in-out;
    cursor:pointer;
    margin-top: 70px;
}
.bottom-buttons button:hover{
    background-color: red;
    color:white;
}
.movie-box{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    background:linear-gradient(to right, #000000, rgb(228, 70, 17));
    border-radius: 10px;
    box-shadow: 0px 0px 10px #000;
    padding: 10px;
    z-index:100;
}
.search-outerbox{
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    height: 20vh;
    position:absolute;
    background:url('src/assets/johnwick.jpg');
    background-size: stretch;
    box-shadow: 0px 0px 20px #000;
    border-radius: 10px;
}
.search-outerbox input{
    width: 400px;
    height: 25px;
    border-radius: 5px;
    border: none;
    background-color: #fff;
    font-size: 20px;
    color: #000;
    margin: 10px;
    padding:10px;
    outline:none;
}
.search-movie{
    width: 100px;
    height: 40px;
    border-radius: 10px;
    border: none;
    background-color: rgb(255, 0, 0);
    font-size: 20px;
    color: rgb(255, 255, 255);
    cursor:pointer;
    z-index:10000;
    margin:10px;
    transition: all 0.2s ease-in-out;
}

.search-movie:hover{
    transform:scale(1.1);
    background-color:red;
}
.search-innerbox{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background-color: transparent;
    border-radius: 10px;
    position:relative;
    padding: 10px;
    top:0;
}
.wave {
    background-color: transparent;
    width: 100vw;
    height: 80vh;
    position: absolute;
    display: none;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.wave-inner {
    width: 10px;
    height: 15vh;
    margin: 5px;
}

@keyframes wave {
    0% {
        transform: translateY(0) scale(1);

         /* transform: rotate(0deg); */
    }

    25% {
        transform: translateY(-100px) scale(0);

        /* transform: rotate(90deg); */
    }

    50% {
        transform: translateY(0) scale(1);

        /* transform: rotate(0deg); */
    }

    75% {
        transform: translateY(100px) scale(0);

        /* transform: rotate(90deg); */
    }

    100% {
        transform: translateY(0) scale(1);

        /* transform: rotate(0deg); */
    }

}


</style>