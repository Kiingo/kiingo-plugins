# Kiingo Plugins

A collection of specialized plugins for AI-powered business operations.

## Available Plugins

### Vistage Chair Toolkit

Complete toolkit for peer advisory group facilitators including Vistage Chairs, EO moderators, YPO forum officers, and peer advisory group leaders.

**Features:**
- **Meeting Architect**: Design complete meetings with agendas, exercises, facilitation scripts, energy management, and member materials
- **Issue Processing**: Advanced 5-step issue processing with root cause analysis and accountability systems
- **Exercise Lab**: Generate decision-forcing exercises with facilitation scripts and worksheets
- **Curriculum Toolkit**: Design 12-month strategic curricula with member lifecycle management
- **Humanizer**: Remove AI-generated writing patterns for natural, human-sounding text

**Commands:**
- `/meeting-prep [theme]` - Quick-start a complete meeting design
- `/exercise [topic]` - Generate decision-forcing exercises
- `/check-in [context]` - Get curated check-in and icebreaker questions

See [vistage-chair-toolkit/README.md](vistage-chair-toolkit/README.md) for full documentation.

## Installation

Each plugin is available as a `.plugin` file that can be installed directly.

## Development

To add or modify a plugin:
1. Create a directory with your plugin name
2. Include `SKILL.md` files for each skill
3. Include command files in a `commands/` directory
4. Add a `README.md` with plugin overview
5. Create a `.plugin` binary for distribution

