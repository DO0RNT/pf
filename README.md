# Nguyễn Hồng Thái

Four static pages: Home, Work, About, and Contact. Shared teal/mint palette, editorial typography, responsive navigation, page entry reveals, cross-document view transitions where supported, three rotating project introductions, embedded image/PDF previews, and accessible attachment dialogs.

The homepage also displays The Starry Night, Der Wanderer über dem Nebelmeer, and a portrait of Leonardo da Vinci in original SVG wooden frames. The gallery uses staggered entrance and brief settling animations, respects reduced motion, and retains a small initials avatar for the missing personal portrait. Captions and a native Artwork credits disclosure link to the image sources; see `dist/assets/art/SOURCES.md`.

Three supplied landscape photos form a faded homepage background: the wide meadow provides the main sky and horizon, the cloudier field blends into the lower left, and the close-up grass accents the lower right. Feathered masks and a stronger off-white wash on the text side keep the scenery subordinate to the name and introduction. Mobile has its own crop and placement rules. The original uploaded PNG files are preserved in `dist/assets/backgrounds`.

## Personalize

Edit `dist/assets/content.js`. Unknown facts stay null and display as clearly marked placeholders. Do not substitute fabricated contact details, credentials, or achievements. Set `portrait` to a local image path; set each project's attachment to `{ type: 'image' | 'pdf', src: 'assets/your-file.ext', alt: 'An accurate description' }`. Add the files beneath `dist/assets`. Each attachment is embedded directly in its project, with an enlarged preview and an original-file link. Set `placeholder: false` for a real file.

The main page heading uses the full name Nguyễn Hồng Thái. The shared header contains right-aligned navigation. Exactly three projects appear in the carousel, each with an introduction, role, and achievements. Three blank PNG attachments are shown until real files are supplied. Selection is shareable using `work.html?project=1`, `2`, or `3`.

## Motion

- Staggered name entry, portrait reveal, restrained hover feedback, and viewport reveals.
- Native page view transitions with a CSS entrance fallback.
- Eight-second project rotation, animated selection marker, and a progress line.
- Previous/Next, project selectors, Pause/Play, and keyboard left/right controls.
- Manual interaction pauses rotation; mouse hover, background tabs, and attachment previews suspend rotation.
- Reduced-motion preferences disable automatic rotation and motion effects.
- Native modal dialogs support Escape and return focus to the opener.

## Regenerate

`python3 scripts/render-pages.py` regenerates the HTML shell. Personal content is kept in `dist/assets/content.js`. No build dependencies, third-party fonts, or remote requests are needed to render the pages. All deployable static files are in `dist`. This export also supports opening local files directly.
