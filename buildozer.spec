name: Build APK

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Build APK
        uses: digreatbrian/buildozer-action@v2
        with:
          workdir: .
          buildozer_version: stable

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: budget-tracker-apk
          path: ./*.apk