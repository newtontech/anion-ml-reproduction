# Anion Optimization Reproduction Report - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | Anion Optimization ML Reproduction Report |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 12 |
| **Design Style** | General Consulting (B) |
| **Target Audience** | Research group / lab meeting |
| **Use Case** | Academic reproduction report |
| **Created Date** | 2026-04-06 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | Left/Right 60px, Top 50px, Bottom 40px |
| **Content Area** | 1160×630 (60px from left, 50px top, 40px bottom) |

---

## III. Visual Theme

### Theme Style

- **Style**: General Consulting — Data clarity first
- **Theme**: Light theme
- **Tone**: Professional, scientific, data-driven

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | Page background |
| **Secondary bg** | `#F5F7FA` | Card background, section background |
| **Primary** | `#1565C0` | Title decorations, key sections, headers (Technology Blue) |
| **Accent** | `#E74C3C` | Data highlights, key findings, positive class (High Eb) |
| **Secondary accent** | `#3498DB` | Secondary emphasis, Low Eb class |
| **Body text** | `#2C3E50` | Main body text |
| **Secondary text** | `#5D6D7E` | Captions, annotations |
| **Tertiary text** | `#95A5A6` | Supplementary info, footers |
| **Border/divider** | `#DCE1E8` | Card borders, divider lines |
| **Success** | `#27AE60` | Positive indicators, good results |
| **Warning** | `#E74C3C` | Attention markers |

### Gradient Scheme

```xml
<!-- Title bar gradient -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#1565C0"/>
  <stop offset="100%" stop-color="#1976D2"/>
</linearGradient>

<!-- Background decorative gradient -->
<radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
  <stop offset="0%" stop-color="#1565C0" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#1565C0" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Recommended preset**: P1 (Modern business/tech)

| Role | Chinese | English | Fallback |
| ---- | ------- | ------- | -------- |
| **Title** | Microsoft YaHei | Arial | SimHei |
| **Body** | Microsoft YaHei | Calibri | Arial |
| **Code** | - | Consolas | Monaco |
| **Emphasis** | SimHei | Arial Black | Microsoft YaHei |

**Font stack**: `'Microsoft YaHei', 'Calibri', 'Arial', sans-serif`

### Font Size Hierarchy

**Baseline**: Body font size = 18px (dense content, 6+ items per page)

| Purpose | Ratio | Size | Weight |
| ------- | ----- | ---- | ------ |
| Cover title | 2.5x | 48px | Bold |
| Chapter title | 2x | 36px | Bold |
| Content title | 1.5x | 28px | Bold |
| Subtitle | 1.2x | 22px | SemiBold |
| **Body content** | **1x** | **18px** | Regular |
| Annotation | 0.75x | 14px | Regular |
| Page number | 0.6x | 11px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 60px — Chapter title with blue left bar accent
- **Content area**: 580px — Main content, charts, data
- **Footer area**: 30px — Page number, paper reference

### Common Layout Modes

| Mode | Suitable Scenarios |
| ---- | ----------------- |
| **Single column centered** | Cover, conclusion |
| **Left-right split (4:6)** | Image-text mix |
| **Left-right split (5:5)** | Comparisons |
| **Three-column cards** | Feature lists, process steps |
| **Top-bottom split** | Wide images + text |

### Spacing Specification

| Element | Value |
| ------- | ----- |
| Card gap | 24px |
| Content block gap | 28px |
| Card padding | 24px |
| Card border radius | 10px |
| Icon-text gap | 10px |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/`
- **Usage method**: Placeholder format `{{icon:category/icon-name}}`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| Dataset | `{{icon:science/flask}}` | Slide 03 |
| ML Model | `{{icon:development/cpu}}` | Slide 05, 07 |
| Feature | `{{icon:interface/filter}}` | Slide 06 |
| Check/Success | `{{icon:interface/check-circle}}` | Slide 09, 10 |
| Chart | `{{icon:editor/pie-chart}}` | Slide 08 |
| Research | `{{icon:science/molecule}}` | Slide 02 |

---

## VII. Chart Reference List

| Chart Type | Reference Template | Used In |
| ---------- | ------------------ | ------- |
| grouped_bar_chart | `templates/charts/grouped_bar_chart.svg` | Slide 05 (model comparison) |
| horizontal_bar_chart | `templates/charts/horizontal_bar_chart.svg` | Slide 06 (feature importance) |
| kpi_cards | `templates/charts/kpi_cards.svg` | Slide 04 (data summary KPIs) |

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Status |
| -------- | --------- | ----- | ------- | ---- | ------ |
| corr_matrix_all19.png | 3367×2974 | 1.13 | Feature correlation matrix | Diagram | Existing |
| feature_distributions.png | 5367×5306 | 1.01 | Feature distribution by class | Diagram | Existing |
| feature_importance_r1.png | 2369×1764 | 1.34 | RF importance (Round 1) | Diagram | Existing |
| feature_importance_top4.png | 1770×1166 | 1.52 | Top 4 feature importance | Diagram | Existing |
| feature_target_corr.png | 2369×2364 | 1.00 | Feature-target correlation | Diagram | Existing |
| lr_coefficients_round1.png | 2369×1764 | 1.34 | LR coefficients (R1) | Diagram | Existing |
| lr_coefficients_r2.png | 2368×1764 | 1.34 | LR coefficients (R2) | Diagram | Existing |
| roc_comparison.png | 4170×1779 | 2.34 | ROC R1 vs R2 comparison | Diagram | Existing |
| roc_curves_r2.png | 2064×1764 | 1.17 | ROC curves (4 features) | Diagram | Existing |
| roc_mean_cv.png | 1764×1464 | 1.20 | Mean ROC with CV band | Diagram | Existing |
| roc_mean_cv_r2.png | 1764×1464 | 1.20 | Mean ROC with CV band (R2) | Diagram | Existing |

---

## IX. Content Outline

### Part 1: Introduction

#### Slide 01 - Cover

- **Layout**: Single column centered with blue gradient header band
- **Title**: Anion Optimization for Bifunctional Surface Passivation — ML Workflow Reproduction
- **Subtitle**: Xu, J. et al. Nat. Mater. 22, 1507-1514 (2023) — Reproduction Report
- **Info**: 2026-04-06

#### Slide 02 - Paper Background

- **Layout**: Left-right split (4:6), left side key info cards, right side methodology flow
- **Title**: Research Background
- **Content**:
  - Paper: Anion optimization for perovskite solar cells
  - Goal: Screen PH anions for surface passivation via ML
  - 267 PH anions, DFT binding energy calculations
  - Binary classification: High Eb (>3 eV) vs Low Eb (<=3 eV)
  - Key result: ROC AUC = 0.87 ± 0.06 (Random Forest, 4 features)

### Part 2: Data & Feature Engineering

#### Slide 03 - Dataset Overview

- **Layout**: Three-column cards (top) + bottom image
- **Title**: Dataset Overview: 267 PH Anions
- **Content**:
  - Card 1: 267 samples, 19 features
  - Card 2: 201 High Eb (75.3%), 66 Low Eb (24.7%)
  - Card 3: Feature categories: Electronic, Structural, Elemental, Fundamental
  - Image: `feature_target_corr.png` (feature-target correlation bar chart)

#### Slide 04 - Feature Engineering

- **Layout**: Left-right split (5:5)
- **Title**: Feature Engineering & Preprocessing
- **Content** (left):
  - Step 1: Remove MPI, La (highly correlated, |r| > 0.85) → 17 features
  - Step 2: Stratified train/test split 85%/15%
  - Step 3: Standardization (zero mean, unit variance)
  - Train: 226, Test: 41
- **Content** (right):
  - Image: `corr_matrix_all19.png` (correlation matrix heatmap)

### Part 3: ML Training

#### Slide 05 - Round 1 Results (17 Features)

- **Layout**: Top data table + bottom chart area
- **Title**: Round 1: 5 Models with 17 Features
- **Content**:
  - Model results table:
    - Random Forest: AUC=0.9581, Acc=0.8780
    - Gradient Boosting: AUC=0.9516, Acc=0.8293
    - XGBoost: AUC=0.9387, Acc=0.8537
    - Logistic Regression: AUC=0.8774, Acc=0.8537
    - SVC: AUC=0.8839, Acc=0.8780
  - RF 10-fold CV: AUC = 0.7486 ± 0.0772
  - Image: `feature_importance_r1.png`

#### Slide 06 - Feature Selection

- **Layout**: Left-right split (5:5)
- **Title**: Feature Selection: Top 4 Features
- **Content** (left):
  - Identified via RF importance + LR coefficients
  - Top 4: num_O, TPSA, HBA, HOMO
  - Physical interpretation:
    - num_O: More oxygen → more Pb2+ coordination sites
    - TPSA: Larger polar surface → more hydrogen bonding
    - HBA: More H-bond acceptors → stronger interaction
    - HOMO: Lower HOMO → higher electronegativity
- **Content** (right):
  - Image: `lr_coefficients_round1.png`

#### Slide 07 - Round 2 Results (4 Features)

- **Layout**: Top data table + bottom charts
- **Title**: Round 2: 5 Models with 4 Features
- **Content**:
  - Model results table:
    - Random Forest: AUC=0.8984, Acc=0.9024
    - Gradient Boosting: AUC=0.9161, Acc=0.9512
    - XGBoost: AUC=0.9161, Acc=0.9024
    - Logistic Regression: AUC=0.8452, Acc=0.8537
    - SVC: AUC=0.7645, Acc=0.8780
  - RF 10-fold CV: AUC = 0.7817 ± 0.0679
  - Paper target: AUC = 0.87 ± 0.06

### Part 4: Results Comparison

#### Slide 08 - ROC Curve Comparison

- **Layout**: Single image (top-bottom split)
- **Title**: ROC Curve Comparison: Round 1 vs Round 2
- **Content**:
  - Image: `roc_comparison.png` (side-by-side ROC curves)
  - Caption: Left: 17 features, Right: 4 features (num_O, TPSA, HBA, HOMO)

#### Slide 09 - Feature Importance & Coefficients

- **Layout**: Left-right split (5:5)
- **Title**: Feature Importance Analysis (Round 2)
- **Content** (left):
  - Image: `feature_importance_top4.png`
  - RF feature importance ranking
- **Content** (right):
  - Image: `lr_coefficients_r2.png`
  - LR coefficients for 4 features

#### Slide 10 - Mean ROC with CV

- **Layout**: Left-right split (5:5)
- **Title**: Cross-Validation Results (10-fold)
- **Content** (left):
  - Image: `roc_mean_cv.png` (Round 1 mean ROC)
  - AUC = 0.7486 ± 0.0772
- **Content** (right):
  - Image: `roc_mean_cv_r2.png` (Round 2 mean ROC)
  - AUC = 0.7817 ± 0.0679

### Part 5: Conclusion

#### Slide 11 - Reproduction Summary

- **Layout**: Three-column summary + bottom key findings
- **Title**: Reproduction Summary
- **Content**:
  - Column 1: Dataset — 267 samples, 19→17→4 features
  - Column 2: Best model — GB: AUC=0.9161 (4 features)
  - Column 3: Paper comparison — AUC 0.87 ± 0.06
  - Key findings confirmed:
    1. More num_O → stronger Eb
    2. Larger TPSA → stronger Eb
    3. More HBA → stronger Eb
    4. Lower HOMO → stronger Eb

#### Slide 12 - Thank You

- **Layout**: Single column centered
- **Title**: Thank You
- **Subtitle**: Questions & Discussion
- **Info**: Paper DOI: 10.1038/s41563-023-01705-y

---

## X. Speaker Notes Requirements

- **File naming**: Match SVG names (e.g., `01_cover.md`)
- **Notes style**: Formal academic
- **Presentation purpose**: Report
- **Total duration**: ~15 minutes

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `clipPath`, `mask`, `<style>`, `class`, `foreignObject`
6. FORBIDDEN: `textPath`, `animate*`, `script`, `marker`/`marker-end`
7. Arrows use `<polygon>` triangles instead of `<marker>`

### PPT Compatibility Rules:

- `<g opacity="...">` FORBIDDEN (group opacity); set on each child element individually
- Image transparency uses overlay mask layer (`<rect fill="bg-color" opacity="0.x"/>`)
- Inline styles only; external CSS and `@font-face` FORBIDDEN

---

## XII. Design Checklist

### Pre-generation

- [x] Content fits page capacity
- [x] Layout mode selected correctly
- [x] Colors used semantically

### Post-generation

- [ ] viewBox = `0 0 1280 720`
- [ ] No `<foreignObject>` elements
- [ ] All text readable (>=14px)
- [ ] Content within safe area
- [ ] All elements aligned to grid
- [ ] Same elements maintain consistent style
- [ ] Colors conform to spec
- [ ] CRAP four-principle check passed

---

## XIII. Next Steps

1. ✅ Design spec complete
2. **Next step**: Invoke **Executor** role to generate SVGs (all images are existing — no AI generation needed)
