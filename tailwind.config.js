/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.html"],
    theme: {
        extend: {
            colors: {
                primary: "#DE0000",
                primaryaccent: "#e91613",
                danger: "#f44336",
                lightshade: "#f1f1eb",
                lightaccent: "#b68f74",
                lightaccenthover: "#a77858",
                darkaccent: "#bc6787",
                darkshade: "#131419",
                woodsmoke: "#131419",
                pesto: "#7b813e",
                chilleanfire: "#f87106",
            },
        },
    },
    plugins: [
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
    ],
}

