# KhawrizmOS

> **Sovereign arm64 Linux — built in Riyadh.**  
> No telemetry. No Microsoft. No Google. No Apple.

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Platform: arm64](https://img.shields.io/badge/Platform-arm64-blue.svg)]()
[![Status: LIVE](https://img.shields.io/badge/Status-LIVE-brightgreen.svg)]()

## What this is

KhawrizmOS is a sovereign Linux distribution for arm64. Every default has been audited. Every telemetry endpoint is blocked at the kernel level by the **Phalanx Protocol** before any process can send data out.

This is not a skin on Ubuntu. This is a deliberate, opinionated OS for people who refuse to be surveilled.

## Quick Start

```bash
# Verify before flashing
sha256sum live-image-arm64.hybrid.iso
# Expected: 5dfd6f7f349eb144b36899a21bde765231a1194f1db3dd0182e29ef4ed6eab9f

# Flash to USB (Linux/macOS)
sudo dd if=live-image-arm64.hybrid.iso of=/dev/sdX bs=4M status=progress

# Flash to USB (Windows — Balena Etcher)
# https://etcher.balena.io
```

## What makes it sovereign

- **Phalanx Protocol** — Linux Security Module. Blocks telemetry at ring 0, before any process.
- **Niyah Engine v2** — Arabic-first AI shell. 5 dialects. Fully on-device. Zero cloud.
- **Haven Desktop** — AI overlay. Does not spy.
- **KHZ CLI** — `khz status`, `khz haven build`, `khz drive sync`

## Architecture

```
Ring 0:  Phalanx LSM     (blocks telemetry before any process can send)
Ring 1:  KhawrizmOS Kernel (patched — telemetry IPs nullrouted)
Ring 2:  Niyah Engine    (Arabic AI — on-device, no API keys)
Ring 3:  Haven Desktop + KHZ CLI
```

## No cloud required

KhawrizmOS runs 100% offline. Every feature works without internet. Cloud sync via KhawrizmDrive is opt-in and client-side encrypted.

## Part of the Sovereign Stack

| Component | Status |
|-----------|--------|
| [Haven IDE](../os-haven) | 🔨 ide.khawrzm.com |
| [Three-Lobe AI Core](../GraTech-Nexus-Prime) | ✅ LIVE |
| [Comet-X Extension](../comet-x) | ✅ LIVE |
| K-Forge P2P VCS | 📋 Q3 2026 |

---

**KHAWRIZM · الخوارزمية دائماً تعود للوطن**  
iqd@hotmail.com · Shammar403@gmail.com · [@khawrzm](https://x.com/kharzm)
