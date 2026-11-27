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

Keep the profile short enough to read in one sitting, around 500 words. Three projects get a short paragraph and a link to try them; everything else stays in a one-line table or in `PROJECTS.md`. Use direct first-person language, contractions, specific projects, and occasional dry asides. Let the humor come from Fred’s actual interests: Laser Loon, Ducky, Costco, and the unusual career route. Keep project descriptions factual and put the wider inventory in `PROJECTS.md`.

The November 16 rewrite draws on the structure, plain-language, and meaning-preservation ideas in [Lynote’s rewriting techniques](https://github.com/lynote-ai/humanize-text/blob/main/docs/techniques.md). Those ideas were applied directly during editing; the external API and translation pipeline was not run. No detector score was used as a quality claim.

## Keeping it useful

- Recheck the bio when employment or location changes.
- Recheck a featured project’s README before changing its description or status.
- Keep research, preview, beta, and device-validation limitations attached to the relevant project.
- When a repository becomes private or moves, update or remove its public link.
- Review the guide and suggested pins when the main focus of the work changes.
- Keep the banner self-contained: SVG only, with no scripts, external fonts, or remote assets. The text introduction must remain understandable if images do not load.

The profile intentionally has no activity scraper, scheduled workflow, tracking badge, external statistics image, or generated feed to maintain. The banner comes in two versions, `assets/profile-banner-dark.svg` and `assets/profile-banner-light.svg`, swapped by a `<picture>` element so it matches the viewer’s GitHub theme. Change both together.
