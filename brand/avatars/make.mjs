// Builds the 4 channel avatars as SVG, then renders 2000x2000 PNGs with headless Chrome.
// Run: node brand/avatars/make.mjs
import { writeFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const DIR = dirname(fileURLToPath(import.meta.url));
const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const INK = "#0d1010";

// Base character, traced from Ark's Notion avatar (coordinates in a 1932 box).
const arrowBehind = `
  <path d="M280 952 L1505 938" stroke="${INK}" stroke-width="20" fill="none"/>`;
const arrowFront = `
  <path d="M262 955 L398 896 C381 918 371 935 371 952 C371 970 380 990 390 1008 Z" fill="${INK}"/>
  <path d="M1498 938 L1528 872 L1662 860 L1624 936 L1656 1016 L1518 1004 Z" fill="${INK}"/>`;

const faceFill = `
  <path d="M630 945 C625 1150 680 1350 820 1460 C900 1522 1020 1540 1110 1490
           C1210 1430 1280 1320 1305 1205 C1360 1190 1440 1140 1440 1060
           C1440 1000 1400 975 1375 985 L1300 940 L965 640 Z" fill="#fff"/>`;

const faceLines = `
  <g stroke="${INK}" stroke-width="21" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M630 945 C625 1150 680 1350 820 1460 C900 1522 1020 1540 1110 1490 C1210 1430 1280 1320 1305 1205"/>
    <path d="M1305 1205 C1360 1190 1440 1140 1440 1060 C1440 1000 1400 975 1375 985"/>
    <path d="M578 990 C520 1010 500 1090 545 1150 C565 1175 585 1190 602 1197"/>
    <path d="M930 1008 C935 1060 925 1110 905 1150 C885 1195 895 1225 935 1240"/>
    <path d="M878 1310 C940 1290 1020 1258 1075 1262 C1105 1265 1110 1300 1100 1330
             C1085 1370 1020 1390 960 1395 C910 1398 870 1390 864 1355 C860 1330 862 1315 878 1310 Z"/>
    <path d="M925 1302 L928 1390 M975 1288 L1000 1386 M1030 1274 L1060 1350" stroke-width="17"/>
    <path d="M738 1050 C760 1032 800 1026 840 1030 C862 1032 880 1036 892 1040" stroke-width="17"/>
    <path d="M1022 1042 C1060 1030 1110 1026 1172 1046" stroke-width="17"/>
    <path d="M765 912 C820 910 880 916 902 928 C910 933 912 940 910 946" stroke-width="27"/>
    <path d="M972 938 C1020 924 1080 914 1132 918" stroke-width="27"/>
  </g>
  <path d="M790 1040 C790 1066 802 1082 813 1082 C826 1082 836 1066 836 1040 Z" fill="${INK}"/>
  <path d="M1078 1036 C1078 1064 1090 1080 1101 1080 C1114 1080 1124 1064 1124 1036 Z" fill="${INK}"/>`;

const hair = `
  <g fill="${INK}">
    <path d="M640 945 C560 962 505 900 512 800 C520 660 640 540 820 522 C900 515 950 530 968 560
             C975 600 965 630 955 650 C900 760 800 860 640 945 Z"/>
    <path d="M965 640 C950 560 980 470 1060 425 C1180 380 1330 440 1420 540 C1490 620 1515 780 1495 870
             C1480 920 1400 945 1300 940 C1180 900 1050 790 965 640 Z"/>
    <ellipse cx="912" cy="462" rx="46" ry="31" transform="rotate(25 912 462)"/>
  </g>`;

// Topic props, drawn in the character's own coordinates so they sit on the head.
// `scale`/`dy` shrink and shift the whole drawing so it fits a circle crop.
// `color` is the channel's background for the *-color.png version; "BG" in a prop
// marks a gap stroke that should match the background.
const variants = {
  psych: {
    color: "#cbb9f2",
    scale: 0.9, dx: -114, dy: 157,
    front: `
      <g stroke="${INK}" stroke-width="20" fill="#fff" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="1440" cy="520" r="24"/>
        <circle cx="1520" cy="420" r="38"/>
        <path d="M1440 230 C1415 140 1500 75 1580 105 C1620 45 1740 45 1775 115
                 C1870 105 1925 200 1875 270 C1920 350 1840 430 1760 400
                 C1715 465 1595 460 1570 395 C1475 410 1405 330 1440 230 Z"/>
      </g>
      <g stroke="${INK}" stroke-width="15" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path d="M1662 145 C1615 130 1570 165 1575 210 C1545 235 1555 295 1600 302
                 C1612 340 1660 345 1672 320 L1672 150"/>
        <path d="M1682 145 C1730 130 1775 165 1770 210 C1800 235 1790 295 1745 302
                 C1733 340 1685 345 1672 320"/>
        <path d="M1612 205 C1635 200 1645 218 1640 240 M1605 270 C1628 258 1650 270 1650 288
                 M1732 205 C1709 200 1699 218 1704 240 M1739 270 C1716 258 1694 270 1694 288"/>
      </g>`,
  },
  history: {
    color: "#b5d3a5",
    scale: 1.1, dx: 4, dy: 103,
    front: `
      <path d="M360 650 C500 560 640 240 966 205 C1292 240 1432 560 1572 650
               C1300 535 632 535 360 650 Z" fill="${INK}" stroke="BG" stroke-width="18" stroke-linejoin="round"/>
      <path d="M470 600 C700 520 1232 520 1462 600" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round"/>
      <circle cx="966" cy="470" r="58" fill="#fff"/>
      <circle cx="966" cy="470" r="34" fill="${INK}"/>
      <circle cx="966" cy="470" r="13" fill="#fff"/>`,
  },
  anime: {
    color: "#f6b3c8",
    scale: 1.15, dx: 5, dy: -10,
    eyeShine: true,
    front: `
      <path d="M420 560 C460 640 512 690 512 755 C512 800 477 830 437 830
               C397 830 362 800 362 755 C362 690 397 640 420 560 Z"
            fill="#fff" stroke="${INK}" stroke-width="20" stroke-linejoin="round"/>
      <path d="M405 705 C400 730 402 755 415 775" stroke="${INK}" stroke-width="12" fill="none" stroke-linecap="round"/>
      <g stroke="#fff" stroke-width="26" fill="none" stroke-linecap="round">
        <path d="M1170 560 C1195 590 1225 595 1255 570"/>
        <path d="M1300 550 C1270 575 1265 605 1290 630"/>
        <path d="M1305 675 C1280 650 1250 645 1220 670"/>
        <path d="M1175 685 C1205 660 1210 630 1185 605"/>
      </g>`,
  },
  screen: {
    color: "#f4d060",
    scale: 1.0, dx: 4, dy: 218,
    front: `
      <g transform="rotate(-12 1000 470)">
        <rect x="740" y="250" width="520" height="240" rx="20" fill="${INK}" stroke="BG" stroke-width="18"/>
        <g stroke="#fff" stroke-width="13" stroke-linecap="round">
          <path d="M790 335 L1210 335 M790 410 L1210 410 M1000 335 L1000 450"/>
        </g>
        <g transform="rotate(-20 752 238)">
          <rect x="740" y="170" width="520" height="76" rx="12" fill="#fff" stroke="${INK}" stroke-width="18"/>
          <path d="M800 170 L850 246 L920 246 L870 170 Z M940 170 L990 246 L1060 246 L1010 170 Z
                   M1080 170 L1130 246 L1200 246 L1150 170 Z" fill="${INK}"/>
        </g>
        <circle cx="758" cy="246" r="15" fill="#fff" stroke="${INK}" stroke-width="10"/>
      </g>`,
  },
};

const shine = `
  <circle cx="820" cy="1052" r="8" fill="#fff"/>
  <circle cx="1108" cy="1050" r="8" fill="#fff"/>`;

function svg(v, bg) {
  const c = 966;
  const t = `translate(${c + v.dx} ${c + v.dy}) scale(${v.scale}) translate(${-c} ${-c})`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="2000" height="2000" viewBox="0 0 1932 1932">
  <defs>
    <filter id="ink" x="-5%" y="-5%" width="110%" height="110%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" result="grain"/>
      <feDisplacementMap in="SourceGraphic" in2="grain" scale="5" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
  </defs>
  <rect width="1932" height="1932" fill="${bg}"/>
  <g filter="url(#ink)">
    <g transform="${t}">${arrowBehind}${faceFill}${hair}${faceLines}${v.eyeShine ? shine : ""}${arrowFront}${v.front.replaceAll('"BG"', `"${bg}"`)}</g>
  </g>
</svg>`;
}

for (const [topic, v] of Object.entries(variants)) {
  for (const [name, bg] of [[topic, "#fff"], [`${topic}-color`, v.color]]) {
    const svgPath = join(DIR, `${name}.svg`);
    writeFileSync(svgPath, svg(v, bg));
    execFileSync(CHROME, [
      "--headless=new", "--disable-gpu", "--hide-scrollbars",
      `--screenshot=${join(DIR, `${name}.png`)}`, "--window-size=2000,2000",
      `file://${svgPath}`,
    ], { stdio: "ignore" });
    console.log(`${name}.png`);
  }
}
