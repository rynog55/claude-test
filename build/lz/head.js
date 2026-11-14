const DATA = __DATA__;
const ALBUMS = { i: ['Led Zeppelin', '1969'], ii: ['Led Zeppelin II', '1969'], iii: ['Led Zeppelin III', '1970'], iv: ['Led Zeppelin IV', '1971'], hoth: ['Houses of the Holy', '1973'], pg: ['Physical Graffiti', '1975'], presence: ['Presence', '1976'], itod: ['In Through the Out Door', '1979'], coda: ['Coda', '1982'] };
const SHORTNAME = { i: 'Led Zeppelin', ii: 'II', iii: 'III', iv: 'IV', hoth: 'Houses of the Holy', pg: 'Physical Graffiti', presence: 'Presence', itod: 'In Through the Out Door', coda: 'Coda' };
const SONGS = DATA.map(([title, rows, cols], i) => ({ i, title, rows: new Set([rows]), cols: new Set(cols.split(' ').filter(Boolean)), album: ALBUMS[rows][0] }));
const LYRIC = new Set(['myth', 'water', 'place', 'season', 'unsung']);
const COLS = {
  myth: ['Myth or Middle-earth', 'Norse gods, Tolkien, legend'],
  water: ['Rain, sea or flood', 'In the lyrics'],
  place: ['Names a real place', 'In the lyrics'],
  season: ['Names a season or month', 'In the lyrics'],
  unsung: ['Title never sung', 'Vocal songs only'],
  instrumental: ['Instrumental', 'No vocals'],
  single: ['Released on a single', 'A- or B-side, any year'],
  tsrts: ['On The Song Remains the Same', '1976 live album'],
  o2: ['Played at the 2007 reunion', 'Celebration Day, O2 Arena'],
  sideopen: ['Opens a vinyl side', 'Original LP'],
  closer: ['Closes the album', 'Last track on the LP'],
  long: ['Over 7 minutes', 'Studio version'],
  short: ['Under 3 minutes', 'Studio version'],
  jones: ['John Paul Jones credit', 'Songwriting credit'],
  bonham: ['John Bonham credit', 'Songwriting credit'],
  all4: ['All four credited', 'Page, Plant, Jones, Bonham'],
  pageplant: ['Page and Plant only', 'No other writers'],
  outside: ['Outside writer credited', 'Blues source or traditional'],
  oneword: ['One-word title', 'Ignoring parentheses']
};
const CLASH = [['sideopen','closer'],['long','short'],['pageplant','jones'],['pageplant','bonham'],['pageplant','all4'],['pageplant','outside'],['all4','jones'],['all4','bonham'],['instrumental','unsung'],['instrumental','myth'],['instrumental','water'],['instrumental','place'],['instrumental','season']];
const ROWS = Object.keys(ALBUMS);
const rowLabel = r => [SHORTNAME[r], ALBUMS[r][1]];
