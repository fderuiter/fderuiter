# Profile notes

The root README appears on the GitHub profile when merged into this public repository’s default branch. `PROJECTS.md` provides the wider catalog so the introduction stays readable.

## Suggested account settings

These are copy-ready suggestions. Updating this repository does not change GitHub account fields or pinned repositories.

| Field | Suggested value |
| --- | --- |
| Name | Fred de Ruiter |
| Bio | Clinical data, useful software, and Laser Loon. Minneapolis. Usually building something; occasionally buying it in bulk. |
| Location | Minneapolis, Minnesota |
| Website | https://deruiter.dev |
| Social link | https://www.linkedin.com/in/frederick-de-ruiter-88012467/ |

Suggested pins, in order, matching the README’s featured work:

1. `cadence-clinical` — the main clinical research platform.
2. `OxidizeMath` — Rust, simulation, and mathematical curiosity.
3. `wedding_website` — a full-stack app with a live demo.
4. `imednet-toolkit` — clinical integration and Python.
5. `QRCraftly-web` — a usable public web application.
6. `deruiter.dev` — personal introduction and interactive work.

Pinned cards show each repository’s description, so these are worth updating at the same time:

| Repository | Suggested description | Suggested topics |
| --- | --- | --- |
| `cadence-clinical` | Pre-release operating system for clinical research: one clinical kernel, with EDC, CTMS, RTSM and more built as apps on it. .NET 10 + Vue. | `clinical-trials`, `clinical-research`, `edc`, `cdisc`, `usdm`, `dotnet`, `vue` |
| `OxidizeMath` | Rust math and simulation playground (MRI, chaos, fluids, quantum, epidemiology) with an egui/WebAssembly explorer and maturity-tiered modules. | `rust`, `mathematics`, `simulation`, `egui`, `webassembly`, `lean4` |
| `wedding_website` | Self-hostable wedding website and registry: RSVPs, seating charts, photo uploads, group gifting. Next.js + PostgreSQL. | `wedding-website`, `nextjs`, `typescript`, `postgresql`, `prisma`, `self-hosted`, `rsvp` |
| `QRCraftly-web` | Create, style, scan, and check QR codes in the browser. | `qr-code`, `qr-generator`, `web-app` |

## Editorial sources

Reviewed November 16, 2026. Cadence, OxidizeMath, and the wedding website were re-read on November 27, 2026, and their live demos were opened to confirm they load. The GitHub metadata review covered 38 public repositories: this profile, 27 other non-fork projects, and 10 forks. All 27 original-project READMEs were read. `agy-skills` is not marked as a fork by GitHub, but its README explicitly credits Matt Pocock’s work; that attribution is preserved in the guide.

| Profile material | Public source |
| --- | --- |
| Name, Minneapolis, clinical research focus | [Portfolio hero](https://github.com/fderuiter/deruiter.dev/blob/main/components/Hero.tsx) |
| Career route, research databases, MRI work, ski patrol | [Portfolio biography and timeline data](https://github.com/fderuiter/deruiter.dev/blob/main/lib/i18n-dictionary.ts) |
| Duck and breed | [Portfolio biography spotlight](https://github.com/fderuiter/deruiter.dev/blob/main/components/BioSpotlight.tsx) |
| Costco and public contact links | [Portfolio contact page](https://github.com/fderuiter/deruiter.dev/blob/main/app/contact/page.tsx) |
| Laser Loon authorship and public-domain dedication | [Laser Loon README](https://github.com/fderuiter/Laser_Loon#readme) |
| Wedding website origin story | [wedding_website project history](https://github.com/fderuiter/wedding_website/blob/main/PROJECT_HISTORY.md) |
| Project summaries and maturity qualifications | Each linked repository’s README; GitHub metadata for fork identity and upstream parent |

The introduction uses public biographical material and project documentation. It avoids private repository names, personal contact details absent from the portfolio, unverified impact metrics, clinical approval claims, and optical-transfer throughput promises. Descriptions summarize documented scope; this profile review did not validate the implementations of the other repositories.

## Writing voice

Keep the visible profile short enough to skim: the cards carry the pitch, and each project's longer description sits in a collapsed `<details>` block. Everything else stays in `PROJECTS.md`. Use direct first-person language, contractions, specific projects, and occasional dry asides. Let the humor come from Fred’s actual interests: Laser Loon, Ducky, Costco, and the unusual career route. Keep project descriptions factual and put the wider inventory in `PROJECTS.md`.

The November 16 rewrite draws on the structure, plain-language, and meaning-preservation ideas in [Lynote’s rewriting techniques](https://github.com/lynote-ai/humanize-text/blob/main/docs/techniques.md). Those ideas were applied directly during editing; the external API and translation pipeline was not run. No detector score was used as a quality claim.

## Keeping it useful

- Recheck the bio when employment or location changes.
- Recheck a featured project’s README before changing its description or status.
- Keep research, preview, beta, and device-validation limitations attached to the relevant project.
- When a repository becomes private or moves, update or remove its public link.
- Review the guide and suggested pins when the main focus of the work changes.
- Keep the generated art self-contained: SVG only, with no scripts, web fonts, or remote assets, and CSS animations that stop for viewers who prefer reduced motion. The text must still make sense if images do not load, so every image has full alt text.

## Visual elements

The November 27 refresh made the profile more visual on purpose, while keeping the parts that need upkeep small:

| Element | Source | Upkeep |
| --- | --- | --- |
| Animated banner, project cards, portfolio card | `scripts/build_profile_art.py` writes `assets/banner-*.svg`, `assets/cards/*.svg`, and `assets/portfolio-*.svg` | Edit the `TAGLINES` or `PROJECTS` lists and rerun `python3 scripts/build_profile_art.py`. Every image has a dark and light version swapped by `<picture>`. |
| Laser Loon animation | `assets/src/laser-loon.svg` is Fred’s CC0 flag artwork. The script splits it into loon, fish, eye, and laser layers and writes `assets/laser-loon.svg` | If the source artwork changes, check the element ranges in `loon_parts()`. The script stops with an error if the element count changes. |
| Portfolio screenshot | `assets/src/deruiter-home.webp`, copied from the deruiter.dev README assets | Replace the file and rerun the script when the home page changes. |
| Badges and tech icons | shields.io and skillicons.dev, rendered when the page is viewed | None. If either service goes down, the alt text still reads correctly. |
| Contribution snake | `.github/workflows/snake.yml` runs Platane/snk daily and publishes to the `output` branch | Needs Actions enabled with read and write workflow permissions. Run it once by hand after merging so the image exists. |

Stats cards and streak counters were left out. The public instances are often rate-limited and show broken images, and the live demos say more about the work than commit counts do.
