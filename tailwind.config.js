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
                dangermain: "#cd5e42",
                textcolor: '#d1d1d1',
                background: '#212121',
                lightbg: "#292929",
                infobg: "#21282b",
                dangercolor: "#f44336",
                warning: "#e3b466",
                success: "#7e8e50",
                important: "#cd4277",
                subinfo: "#505050",
                highlight: "#7dd6cf",
                blacky: "#151515",
            },
            keyframes: {
                "gradient-shift": {
                    '0%, 100%': { backgroundPosition: '0% 50%' },
                    '50%': { backgroundPosition: '100% 50%' },
                },
                caret_blink: {
                    '0%, 100%': {
                        opacity: '1',
                    },
                    '50%, 75%': {
                        opacity: '0',
                    }
                },
                typewriter: {
                    to: {
                        left: "100%"
                    }
                }
            },
            animation: {
                gradient: "gradient-shift 15s ease infinite",
                typewriter: "typewriter 2s steps(11) forwards",
                blink: "caret_blink 1.4s ease-in-out infinite",
            }
        }
    },
    plugins: [
        require("@tailwindcss/forms"),
        require("@tailwindcss/typography"),
    ],
}

