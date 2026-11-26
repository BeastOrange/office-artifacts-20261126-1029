from pathlib import Path

# Speculative museum placard interpreting a 21st-century office stapler.
PLACARD_LINE = (
    "Stapler, c. 2024 CE. Pressed steel. Ritual binding device: acolytes squeezed its jaws to fuse scrolls into a single offering. Gift of the Accounts Department."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(PLACARD_LINE + "\n", encoding="utf-8")

    print(PLACARD_LINE)
    print(f"Character count: {len(PLACARD_LINE)}")


if __name__ == "__main__":
    main()
