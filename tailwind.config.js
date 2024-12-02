/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.html"],
    theme: {
        extend: {
            colors: {
                primary: "#0da2d9",
                primarydark: "#1d3a45",
                secondary: '#14a3ad',
                secondarydark: "#1d484b",
                accent: '#43e5b7',
                danger: "#f44336",
                textcolor: '#d1d1d1',
                background: '#212121',
                lightbg: "#292929",
                infobg: "#21282b",
                danger: "#cd5e42",
                warning: "#e3b466",
                success: "#7e8e50",
                important: "#cd4277",
                subinfo: "#505050",
                highlight: "#7dd6cf",
            },
        },
    },
    plugins: [
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
    ],
}

