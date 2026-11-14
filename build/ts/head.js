const DATA = __DATA__;
const ALBUMS = { debut: ['Taylor Swift', '2006'], fearless: ['Fearless', '2008'], speaknow: ['Speak Now', '2010'], red: ['Red', '2012'], '1989': ['1989', '2014'], reputation: ['reputation', '2017'], lover: ['Lover', '2019'], folklore: ['folklore', '2020'], evermore: ['evermore', '2020'], midnights: ['Midnights', '2022'], ttpd: ['The Tortured Poets Department', '2024'], showgirl: ['The Life of a Showgirl', '2025'], vault: ['From the Vault', "Taylor's Version extras"] };
const SONGS = DATA.map(([title, rows, cols], i) => ({ i, title, rows: new Set(rows.split(' ')), cols: new Set(cols.split(' ').filter(Boolean)), album: ALBUMS[rows.split(' ')[0]][0] }));
const LYRIC = new Set(['color', 'rain', 'time', 'place', 'name', 'car', 'number', 'faith']);
const COLS = {
  color: ['Mentions a color', 'In the lyrics'],
  rain: ['Rain in the lyrics', 'Rain or a downpour'],
  time: ['Names a month or season', 'Or a holiday, in the lyrics'],
  place: ['Names a real place', 'City, street or state'],
  name: ["Sings someone's name", 'Not counting Taylor'],
  car: ['Cars or driving', 'In the lyrics'],
  number: ['Sings a number or age', 'In the lyrics'],
  faith: ['God, heaven or holy', 'Religious imagery'],
  single: ['Released as a single', 'Lead-artist single'],
  n1: ['Hot 100 No. 1', 'US chart peak'],
  t10: ['Hot 100 top 10', 'US chart peak'],
  opener: ['Album opener', 'Track 1, standard edition'],
  closer: ['Album closer', 'Last standard track'],
  track5: ['Track 5', 'Standard edition'],
  feat: ['Has a featured artist', 'Credited "featuring"'],
  oneword: ['One-word title', 'Ignoring parentheses'],
  antonoff: ['Co-written with Jack Antonoff', 'Songwriting credit'],
  dessner: ['Co-written with Aaron Dessner', 'Songwriting credit'],
  martin: ['Co-written with Max Martin', 'Songwriting credit'],
  solo: ['Written by Taylor alone', 'No co-writers']
};
const CLASH = [['n1','t10'],['opener','closer'],['opener','track5'],['closer','track5'],['solo','antonoff'],['solo','dessner'],['solo','martin'],['antonoff','martin'],['dessner','martin']];
const ROWS = Object.keys(ALBUMS);
const rowLabel = r => ALBUMS[r];
