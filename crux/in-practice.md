---
layout: crux
title: Crux in practice
permalink: /crux/in-practice/
description: "How I run a project with it."
---

I've been building with Crux (and it's predecessors) for over a year. 

## 1. Define your objective

Set the objective first, and iterate on it until it is clear. It becomes the ruler you measure ADR drift against.
This lives in the `bionic/objectives.md` file. Articulate a clear picture of what you want to create
and lock it in as an objecitve. The rest will follow.

## 2. Plan with a research and a whiteboard session

When you start building, research the problem space. I will often do this interactively in an external system.
I store the results in markdown format and toss them into the inbox.

When you have a clear understanding of the problem space, kick off a whiteboarding session.
The agent will take what you've provided and guide the conversation.

## 3. Build with ADRs and a dev cycle

When it's time to build, work with an architect to craft an ADR that lays out the rules around 
what you are building. Approve it once it looks good and then proceed with the dev cycle.

This really helps lock down requirements for the build to ensure you get the best results.

## 4. Make quick fixes with an iterate cycle

A full dev cycle might take hours, or even days. If you need a quick fix, use the iterate cycle.

It's lighter and faster but doesn't come with the same scrutiny as a full dev cycle.

## 5. Schedule the night gardener

Setup a scheduled job to have the Night Gardener "tend the garden" automatically.

I've been delighted several times by what its come up with.

## 6. Clean the campsite, audit, review, reflect

There are several tools intended to help maintain the health of a long-running project.

You should clean up your campsite and audit your docs between cycles or at least every couple of days.
Review your decisions weekly. Periodically run a retrospective.

## 7. Larger projects: split the repos

I have had great success running a main planing repo with several sub-repos that it manages.
Each sub-repo has its own ADRs and can be managed independently.

The planning repo is responsible for prompting the sub-repos and it drops notes into their inboxes.

## 8. Larger teams: customize the ADR numbering

When several people propose ADRs, the numbers collide. Customize the numbering per repo or per team.

At some point I plan to release a tool to help with this where numbers can be centrally managed.
