import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:automatic_app_test/expandable.dart';

void main() {
  testWidgets('ExpandableCard Test', (WidgetTester tester) async {
    // Define the test values
    const String title = 'Test Title';
    const String description = 'Test Description';

    // Build the ExpandableCard widget
    await tester.pumpWidget(MaterialApp(
      home: Scaffold(
        body: ExpandableCard(title: title, description: description),
      ),
    ));

    // Verify the initial state
    expect(find.text(title), findsOneWidget);
    expect(find.text(description), findsNothing);
    expect(find.byIcon(Icons.expand_more), findsOneWidget);
    expect(find.byIcon(Icons.expand_less), findsNothing);

    // Tap the expand button to expand the card
    await tester.tap(find.byIcon(Icons.expand_more));
    await tester.pump();

    // Verify the expanded state
    expect(find.text(title), findsOneWidget);
    expect(find.text(description), findsOneWidget);
    expect(find.byIcon(Icons.expand_more), findsNothing);
    expect(find.byIcon(Icons.expand_less), findsOneWidget);

    // Tap the collapse button to collapse the card
    await tester.tap(find.byIcon(Icons.expand_less));
    await tester.pump();

    // Verify the collapsed state
    expect(find.text(title), findsOneWidget);
    expect(find.text(description), findsNothing);
    expect(find.byIcon(Icons.expand_more), findsOneWidget);
    expect(find.byIcon(Icons.expand_less), findsNothing);
  });
}