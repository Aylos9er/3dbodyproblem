# 3dbodyproblem
# Interactive Space Simulations in JavaScript

This project contains interactive 2D/3D space simulations built with HTML, JavaScript, and physics/rendering libraries like Cannon.js and Babylon.js. It explores concepts like the N-body problem, gravitational interactions, and particle effects.

## Simulations Included:

* **Three-Body Problem with Particle Dust & Trails (with Info Panel):** A visualization of the classic three-body problem showcasing orbital mechanics with aesthetic particle dust, trail effects, and an informational scrolling panel.
* *(You can list other simulations if you create more)*

## Features

* **N-Body Gravitational Physics:** Utilizes Cannon.js for simulating gravitational forces between multiple bodies.
* **3D Visualization:** Employs Babylon.js for rendering celestial bodies, orbital trails, and particle systems (dust).
* **Interactive Camera Controls:** Standard Babylon.js ArcRotateCamera allows users to pan, zoom, and rotate the view.
* **Informational Panel:** A styled, scrollable text panel (inspired by "origami folding") provides context, lore, or instructions.
* **Adjustable Parameters:** UI elements allow users to reset simulations and adjust parameters like the gravitational constant.
* **Modular Design:** Each simulation is largely self-contained in a single HTML file for ease of use and modification.

## Technologies Used

* **HTML5:** For structuring the web page.
* **CSS3:** For styling the UI elements and the informational panel.
* **JavaScript (ES6+):** For the core simulation logic and interactivity.
* **Babylon.js:** A powerful 3D rendering engine for WebGL.
* **Cannon.js:** A lightweight 3D physics engine.

## Setup and Running

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```
    *(Replace `YOUR_USERNAME` and `YOUR_REPOSITORY_NAME` with your actual GitHub details after you create the repository.)*
    If you've downloaded a specific HTML file, you can skip this step.

2.  **Open the HTML file(s) in a web browser:**
    * Navigate to the project directory on your computer.
    * Open the `three_body_dust_trails_sim_with_panel.html` (or similarly named) file directly in a modern web browser that supports WebGL (like Chrome, Firefox, Edge, Safari).
    * No local server or build process is required for these particular simulations as they rely on CDN-hosted libraries.

## File Structure (Example)


/
|-- three_body_dust_trails_sim_with_panel.html  (Main simulation file)
|-- README.md                                   (This file)
|-- .gitignore                                  (Git ignore file)


## How to Contribute

*(Optional: If you plan for others to contribute)*
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourAmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some YourAmazingFeature'`).
5.  Push to the branch (`git push origin feature/YourAmazingFeature`).
6.  Open a Pull Request.

## License

*(Optional: Choose a license if you wish, e.g., MIT License)*
This project is open source and available under the [MIT License](LICENSE.txt).


