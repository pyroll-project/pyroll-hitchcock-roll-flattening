---
title: PyRoll Hitchcook roll flattening Plugin 
author: [Christoph Renzing]
date: 2022-08-04
---

This plugin provides the analytical roll flattening model developed by J. Hitchcook[^1] and adapted by Bohm and Flaxa[^2]. 
The models are derived from the general theory of elasticity.
According to Hitchcock, roll flattening can be included by determining a flattened roll radius.
Therefore he assumes an elliptical pressure distribution and a circular shape of the contact line. 
For the calculation the roll force and the elastic constants of the roll material are required.
To Calculate the flattened radius following equation is used:


$$ \frac{R_\mathrm{W}}{R_\mathrm{W,0}} = 1 + \frac{16}{\pi} \frac{1- \nu_\mathrm{W}^2}{E_\mathrm{W}} \frac{F_\mathrm{Roll}}{h_\mathrm{eq,0} - s}, \frac{R_\mathrm{W}}{R_\mathrm{W,0}} < 5.235
$$
$$ \frac{R_\mathrm{W}}{R_\mathrm{W,0}} = \left(  \frac{16}{\pi} \frac{1- \nu_\mathrm{W}^2}{E_\mathrm{W}} \frac{F_\mathrm{Roll}}{h_\mathrm{eq,0} - s} \right)^{\frac{2}{3}}, \frac{R_\mathrm{W}}{R_\mathrm{W,0}} > 5.235
$$

Through the dependence on the roll force a fixed point iteration is necessary.

## Usage of the Plugin

The plugin provides implementations of the following core hooks:

`RollPass.roll_poissons_ratio`
:   The rolls material poissons ratio.

`RollPass.roll_youngs_modulus`
:   The rolls material Young's modulus.

`RollPass.nominal_radius_flattened_radius_ratio`
:   The ratio between the flattened and the initial nominal roll radius $R_\mathrm{W}/R_\mathrm{W,0}$. Uses the core hooks `RollPass.nominal_roll_radius`.

One can modify the behavior of the plugin by providing constant attributes or custom implementations of the hooks. The plugin needs no additional material data
or coefficients to be given on the initial profile or on the roll passes. Commonly it should work out of the box, without additional definitions by the user.

[^1]:
Hitchcook, J. H., W. Trinks, Roll neck bearings. Report of A.S.M.E. Special Research Committee on Heavy- Duty Anti-friction Bearings, 1935.

[^2]: Bohm, J., Flaxa, V., Cold Rolling of Thin Stock. Neue Huette, 23 (8), 1978.
