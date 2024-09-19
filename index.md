---
layout: base
title: Student Home 
description: Home Page
image: /images/mario_animation.png
hide: true
---

<!--- Concatenation of site URL to frontmatter image  --->
{% assign sprite_file = site.baseurl | append: page.image %}
<!--- Has is a list variable containing mario metadata for sprite --->
{% assign hash = site.data.mario_metadata %}  
<!--- Size width/height of Sprit images --->
{% assign pixels = 256 %}

<!--- HTML for page contains <p> tag named "Mario" and class properties for a "sprite"  -->

<p id="mario" class="sprite"></p>
  
<!--- Embedded Cascading Style Sheet (CSS) rules, 
        define how HTML elements look 
--->
<style>

  /*CSS style rules for the id and class of the sprite...
  */
  .sprite {
    height: {{pixels}}px;
    width: {{pixels}}px;
    background-image: url('{{sprite_file}}');
    background-repeat: no-repeat;
  }

  /*background position of sprite element
  */
  #mario {
    background-position: calc({{animations[0].col}} * {{pixels}} * -1px) calc({{animations[0].row}} * {{pixels}}* -1px);
  }
</style>

<!--- Embedded executable code--->
<script>
  ////////// convert YML hash to javascript key:value objects /////////

  var mario_metadata = {}; //key, value object
  {% for key in hash %}  
  
  var key = "{{key | first}}"  //key
  var values = {} //values object
  values["row"] = {{key.row}}
  values["col"] = {{key.col}}
  values["frames"] = {{key.frames}}
  mario_metadata[key] = values; //key with values added

  {% endfor %}

  ////////// game object for player /////////

  class Mario {
    constructor(meta_data) {
      this.tID = null;  //capture setInterval() task ID
      this.positionX = 0;  // current position of sprite in X direction
      this.currentSpeed = 0;
      this.marioElement = document.getElementById("mario"); //HTML element of sprite
      this.pixels = {{pixels}}; //pixel offset of images in the sprite, set by liquid constant
      this.interval = 100; //animation time interval
      this.obj = meta_data;
      this.marioElement.style.position = "absolute";
    }

    animate(obj, speed) {
      let frame = 0;
      const row = obj.row * this.pixels;
      this.currentSpeed = speed;

      this.tID = setInterval(() => {
        const col = (frame + obj.col) * this.pixels;
        this.marioElement.style.backgroundPosition = `-${col}px -${row}px`;
        this.marioElement.style.left = `${this.positionX}px`;

        this.positionX += speed;
        frame = (frame + 1) % obj.frames;

        const viewportWidth = window.innerWidth;
        if (this.positionX > viewportWidth - this.pixels) {
          document.documentElement.scrollLeft = this.positionX - viewportWidth + this.pixels;
        }
      }, this.interval);
    }

    startWalking() {
      this.stopAnimate();
      this.animate(this.obj["Walk"], 3);
    }

    startRunning() {
      this.stopAnimate();
      this.animate(this.obj["Run1"], 6);
    }

    startPuffing() {
      this.stopAnimate();
      this.animate(this.obj["Puff"], 0);
    }

    startCheering() {
      this.stopAnimate();
      this.animate(this.obj["Cheer"], 0);
    }

    startFlipping() {
      this.stopAnimate();
      this.animate(this.obj["Flip"], 0);
    }

    startResting() {
      this.stopAnimate();
      this.animate(this.obj["Rest"], 0);
    }

    stopAnimate() {
      clearInterval(this.tID);
    }
  }

  const mario = new Mario(mario_metadata);

  ////////// event control /////////

  window.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") {
      event.preventDefault();
      if (event.repeat) {
        mario.startCheering();
      } else {
        if (mario.currentSpeed === 0) {
          mario.startWalking();
        } else if (mario.currentSpeed === 3) {
          mario.startRunning();
        }
      }
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      if (event.repeat) {
        mario.stopAnimate();
      } else {
        mario.startPuffing();
      }
    }
  });

  //touch events that enable animations
  window.addEventListener("touchstart", (event) => {
    event.preventDefault(); // prevent default browser action
    if (event.touches[0].clientX > window.innerWidth / 2) {
      // move right
      if (currentSpeed === 0) { // if at rest, go to walking
        mario.startWalking();
      } else if (currentSpeed === 3) { // if walking, go to running
        mario.startRunning();
      }
    } else {
      // move left
      mario.startPuffing();
    }
  });

  //stop animation on window blur
  window.addEventListener("blur", () => {
    mario.stopAnimate();
  });

  //start animation on window focus
  window.addEventListener("focus", () => {
     mario.startFlipping();
  });

  //start animation on page load or page refresh
  document.addEventListener("DOMContentLoaded", () => {
    // adjust sprite size for high pixel density devices
    const scale = window.devicePixelRatio;
    const sprite = document.querySelector(".sprite");
    sprite.style.transform = `scale(${0.2 * scale})`;
    mario.startResting();
  });

</script>
<h3>BUTTONS YIPPIE :O</h3>
<p>This button leads to the front page of youtube. I chose this link because youtube is a tool used for alot of things on the internet like coding tutorials maybe and very interseting videos. I also used a little bit of youtube for some help making this website.</p>

<img alt="image of tv" src="https://static1.howtogeekimages.com/wordpress/wp-content/uploads/2023/09/oldstatickytv1.jpg" width="200" height="200">
 <button><a href="https://www.youtube.com">Watch tv??:)</a></button>

<strong>Behold the tv</strong>

 <img alt="pac-man title" src="https://www.phoenixarcade.com/sites/default/files/pacman-marquee-full.jpg" width="200" height="200">
  <button><a href="https://www.google.com/search?si=ACC90nzF_VmFQ6qzGnBNcJ9wQNEp1KvsKw5ihI0insdEjHaILSXJjOGneVpDnQ8cQ6zQh8jL1lAOHzD0HXd1_pAHbZ8h-5m2DXkyh1BnPtyPGMszKdpLJtOb69nOvqxZj-kpn_-NR8IhDyLSRXi6pMzrNsbwG7nNtVALxwRRVz63jfsci3NXMiPKkcUtgJaZHWf6So8rGMWVoy2ZWBInCPO5z7Tc1DefuO-Hc8MsFDu6SUrFV7PRb3R0at8Ak5IqHbcAAwZzAm1CKGUCpUph4HlNsbI0gT-IZw%3D%3D&hl=en-US&shndl=21&shem=vslcca&source=sh%2Fx%2Ffbx%2Fm1%2F1&kgs=c4bd646f747feb1a">Play PacMan(0_0)</a></button>

 <img alt="Tron title" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHLoWYuHnp9pQ77k_qgOsMlxj2oYW4MltRKA&s" width="200" height="200">
  <button><a href="https://archive.org/details/arcade_dotron#">Play Deadly discs</a></button>

  <p> I added these two buttons which were games I really like. I wouldnt have found out about through the internet and Ive been playing these whenever im taking a break from newer games and sharing them with friends.<p>


