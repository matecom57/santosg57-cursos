Preface
=======

In the last couple of years, browsers have become more powerful and are capable
platforms to deliver complex applications and graphics. Most of these, though, are
standard 2D graphics. Most modern browsers have adopted WebGL, which allows
you to not just create 2D applications and graphics in the browser, but also create
beautiful and good performing 3D applications using the capabilities of the GPU.

En los últimos años, los navegadores se han vuelto más potentes y se han convertido en plataformas capaces de ofrecer aplicaciones y gráficos complejos. Sin embargo, la mayoría de estos gráficos son 2D estándar. La mayoría de los navegadores modernos han adoptado WebGL, que permite no solo crear aplicaciones y gráficos 2D directamente en el navegador, sino también crear aplicaciones 3D atractivas y de alto rendimiento aprovechando las capacidades de la GPU.


Programming WebGL directly, however, is very complex. You need to know the
inner details of WebGL and learn a complex shader language to get the most out of
WebGL. Three.js provides a very easy to use JavaScript API around the features of
WebGL, so you can create beautiful 3D graphics without having to learn WebGL
in detail.

Sin embargo, programar directamente en WebGL es muy complejo. Es necesario conocer los detalles internos de WebGL y aprender un lenguaje de sombreado complejo para sacarle el máximo partido. Three.js proporciona una API de JavaScript muy fácil de usar que integra las funcionalidades de WebGL, lo que permite crear impresionantes gráficos 3D sin necesidad de aprender WebGL en profundidad.



Three.js provides a large number of features and APIs that you can use to create 3D
scenes directly in your browser. In this book, you'll learn all the different APIs Three.
js has to offer through lots of interactive examples and code samples.

Three.js ofrece una gran cantidad de funciones y API que puedes usar para crear escenas 3D directamente en tu navegador. En este libro, aprenderás todas las API que Three.js ofrece a través de numerosos ejemplos interactivos y muestras de código.


**What this book covers**

Chapter 1, Creating Your First 3D Scene with Three.js, covers the basic steps you need
to take to get started with Three.js. You'll immediately create your first Three.js scene
and at the end of this chapter, you'll be able to create and animate your first 3D scene
directly in your browser.

El capítulo 1, «Creando tu primera escena 3D con Three.js», cubre los pasos básicos que necesitas seguir para empezar a usar Three.js. Crearás inmediatamente tu primera escena con Three.js y, al final de este capítulo, podrás crear y animar tu primera escena 3D directamente en tu navegador.


Chapter 2, Basic Components That Make Up a Three.js Scene, explains the basic
components that you need to understand when working with Three.js. You'll learn
about lights, meshes, geometries, materials, and cameras. In this chapter, you will
also get an overview of the different lights Three.js provides and the cameras you
can use in your scene.

El capítulo 2, Componentes básicos de una escena en Three.js, explica los componentes básicos que necesitas comprender al trabajar con Three.js. Aprenderás sobre luces, mallas, geometrías, materiales y cámaras. En este capítulo, también obtendrás una descripción general de las diferentes luces que ofrece Three.js y las cámaras que puedes usar en tu escena.


Chapter 3, Working with the Different Light Sources Available in Three.js, dives deeper
into the different lights you can use in your scene. It shows examples and explains
how to use a spotlight, a direction light, an ambient light, a point light, a hemisphere
light, and an area light. Additionally, it also shows how to apply a lens flare effect on
your light source.

El capítulo 3, «Trabajando con las distintas fuentes de luz disponibles en Three.js», profundiza en los diferentes tipos de luz que puedes usar en tu escena. Muestra ejemplos y explica cómo usar un foco, una luz direccional, una luz ambiental, una luz puntual, una luz hemisférica y una luz de área. Además, también muestra cómo aplicar un efecto de destello de lente a la fuente de luz.


Chapter 4, Working with Three.js Materials, talks about the materials available in
Three.js that you can use on your meshes. It shows all the properties you can set to
configure the materials for your specific use and provides interactive examples to
experiment with the materials that are available in Three.js.

El capítulo 4, "Trabajando con materiales de Three.js", trata sobre los materiales disponibles en Three.js que puedes usar en tus mallas. Muestra todas las propiedades que puedes configurar para adaptar los materiales a tus necesidades específicas y proporciona ejemplos interactivos para experimentar con los materiales disponibles en Three.js.


Chapter 5, Learning to Work with Geometries, is the first of two chapters that explores
all the geometries that are provided by Three.js. In this chapter, you'll learn how to
create and configure geometries in Three.js and can experiment using the provided
interactive examples with geometries (such as plane, circle, shape, cube, sphere,
cylinder, torus, torusknot, and polyhedron).

El capítulo 5, Aprender a trabajar con geometrías, es el primero de dos capítulos que exploran todas las geometrías que ofrece Three.js. En este capítulo, aprenderás a crear y configurar geometrías en Three.js y podrás experimentar con los ejemplos interactivos proporcionados (como plano, círculo, figura, cubo, esfera, cilindro, toroide, nudo de toroide y poliedro).


Chapter 6, Advanced Geometries and Binary Operations, continues where Chapter 5,
Learning to Work with Geometries, left off. It shows you how to configure and use the
more advanced geometries provided by Three.js such as convex and lathe. In this
chapter, you'll also learn how to extrude 3D geometries from 2D shapes, and how
you can create new geometries by combining geometries using binary operations.

El capítulo 6, Geometrías avanzadas y operaciones binarias, continúa donde terminó el capítulo 5, Aprender a trabajar con geometrías. Muestra cómo configurar y usar las geometrías más avanzadas que ofrece Three.js, como convexas y de torno. En este capítulo, también aprenderá a extruir geometrías 3D a partir de formas 2D y cómo crear nuevas geometrías combinándolas mediante operaciones binarias.


Chapter 7, Particles, Sprites, and the Point Cloud, explains how to use a point cloud
from Three.js. You'll learn how to create a point cloud from scratch and from existing
geometries. In this chapter, you'll also learn how you can modify the way the
individual points look through the use of sprites and point cloud materials.

El capítulo 7, Partículas, Sprites y Nube de Puntos, explica cómo usar una nube de puntos en Three.js. Aprenderás a crear una nube de puntos desde cero y a partir de geometrías existentes. En este capítulo, también aprenderás a modificar la apariencia de los puntos individuales mediante el uso de sprites y materiales de nube de puntos.


Chapter 8, Creating and Loading Advanced Meshes and Geometries, shows you how to
import meshes and geometries from external sources. You'll learn how to use Three.
js' internal JSON format to save geometries and scenes. This chapter also explains
how to load models from formats such as OBJ, DAE, STL, CTM, PLY, and many
more.

El capítulo 8, «Creación y carga de mallas y geometrías avanzadas», muestra cómo importar mallas y geometrías desde fuentes externas. Aprenderá a usar el formato JSON interno de Three.js para guardar geometrías y escenas. Este capítulo también explica cómo cargar modelos desde formatos como OBJ, DAE, STL, CTM, PLY y muchos más.


Chapter 9, Animations and Moving the Camera, explores the various types of animations
you can use to make your scene come alive. You'll learn how to use the Tween.js
library together with Three.js, and how to work with animation models based on
morphs and skeletons.

El capítulo 9, Animaciones y movimiento de la cámara, explora los distintos tipos de animaciones que puedes usar para dar vida a tu escena. Aprenderás a usar la biblioteca Tween.js junto con Three.js y a trabajar con modelos de animación basados ​​en transformaciones y esqueletos.


Chapter 10, Loading and Working with Textures, expands on Chapter 4, Working with
Three.js Materials, where materials were introduced. In this chapter, we dive into
the details of textures. This chapter introduces the various types of textures that
are available and how you can control how a texture is applied to your mesh.
Additionally, in this chapter, you are shown how you can directly use the output
from HTML5 video and canvas elements as input for your textures.

El capítulo 10, Carga y trabajo con texturas, amplía el capítulo 4, Trabajo con materiales de Three.js, donde se introdujeron los materiales. En este capítulo, profundizamos en los detalles de las texturas. Se presentan los distintos tipos de texturas disponibles y cómo controlar su aplicación a la malla. Además, se muestra cómo usar directamente la salida de los elementos de vídeo y lienzo de HTML5 como entrada para las texturas.


Chapter 11, Custom Shaders and Render Postprocessing, explores how you can use Three.
js to apply postprocessing effects to your rendered scene. With postprocessing, you
can apply effects such as blur, tiltshift, sepia, and so on, to your rendered scene.
Besides this, you'll also learn how to create your own postprocessing effect and
create a custom vertex and fragment shader.

El capítulo 11, "Sombreadores personalizados y posprocesamiento de renderizado", explora cómo usar Three.js para aplicar efectos de posprocesamiento a la escena renderizada. Con el posprocesamiento, puedes aplicar efectos como desenfoque, tilt-shift, sepia, etc. Además, aprenderás a crear tus propios efectos de posprocesamiento y a diseñar sombreadores de vértices y fragmentos personalizados.


Chapter 12, Adding Physics and Sounds to Your Scene, explains how you can add
physics to your Three.js scene. With physics, you can detect collisions between
objects, make them respond to gravity, and apply friction. This chapter shows you
how to do this with the Physijs JavaScript library. Additionally, this chapter also
shows you how you can add positional audio to a Three.js scene


El capítulo 12, "Añadiendo física y sonidos a tu escena", explica cómo puedes añadir física a tu escena de Three.js. Con la física, puedes detectar colisiones entre objetos, hacer que respondan a la gravedad y aplicar fricción. Este capítulo te muestra cómo hacerlo con la biblioteca JavaScript Physijs. Además, este capítulo también te muestra cómo puedes añadir audio posicional a una escena de Three.js.
